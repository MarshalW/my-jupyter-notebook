import requests
from gne import GeneralNewsExtractor
import os

from llama_index.core import(
    StorageContext, 
    load_index_from_storage,
    get_response_synthesizer,
    DocumentSummaryIndex,
    Document
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import FunctionTool

INDEX_PATH="news-index"

def get_news_data(url):
    response = requests.get(url)
    html = response.text

    extractor = GeneralNewsExtractor()
    data = extractor.extract(html, noise_node_list=[
                               '//div[@class="comment-list"]'])
    data['url']=url
    return data

def load_index(folder_path):
    # 考虑不存在的情况，创建空的索引
    if not os.path.exists(folder_path):
        splitter = SentenceSplitter(chunk_size=1024)
        response_synthesizer = get_response_synthesizer(
            response_mode="tree_summarize", use_async=True,
        )
        
        doc_summary_index = DocumentSummaryIndex.from_documents(
            [],
            transformations=[splitter],
            response_synthesizer=response_synthesizer,
            show_progress=True,
        )
        
        doc_summary_index.storage_context.persist(folder_path)
        
    storage_context = StorageContext.from_defaults(persist_dir=folder_path)
    return load_index_from_storage(storage_context)


def _data2doc(news_data):
    document=Document(text=news_data['content'], 
                  metadata={"title": news_data['title'],
                            'publish_time': news_data['publish_time'],
                            'author': news_data['author'],
                            'url': news_data['url'],
                            'images': news_data['images'],
                           })
    document.doc_id = document.metadata["title"]
    return document

def get_news_summary(url: str) -> str:
    """根据url获取新闻内容, 提示词中应提供url"""
    
    news_data=get_news_data(url)
    document=_data2doc(news_data)
    doc_summary_index=load_index(INDEX_PATH)

    if document.doc_id not in doc_summary_index.ref_doc_info:
        doc_summary_index.insert(document)
        doc_summary_index.refresh([document])
        doc_summary_index.storage_context.persist(INDEX_PATH)

    summary=doc_summary_index.get_document_summary(document.doc_id)

    prompt=f"""
    请根据{summary}, 用中文做有条理的表述。
    """
        
    return prompt

get_news_summary_tool = FunctionTool.from_defaults(
            fn=get_news_summary)

from llama_index.core.tools import QueryEngineTool
from llama_index.core.tools.types import ToolMetadata

def get_query_engine():
    """根据提示词查询信息，提示词不应存在url"""

    # content='查询到的信息: 1. xxx, 2. xxx ...'
    # return f"根据{query}查询到信息\n\n{content}"
    doc_summary_index=load_index(INDEX_PATH)

    return doc_summary_index.as_query_engine(
        response_mode="tree_summarize", 
        streaming=True,
        # similarity_top_k=5
    )

def get_query_engine_tool():
    return QueryEngineTool.from_defaults(
        query_engine=get_query_engine(),
        name="query",
        description="根据提示词查询信息，提示词不应存在url。",
        # return_direct=True,
    )