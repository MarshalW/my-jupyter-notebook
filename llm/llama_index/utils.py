from llama_index.llms.openai_like import OpenAILike
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings

llm = OpenAILike(model="qwen2-7b-6k", 
                 api_base="http://192.168.0.72:3000/v1", 
                 api_key="sk-bJP6QSnUfjAYeYeE505d3eBf63A643BeB0B8E350Df9b7750",
                 is_chat_model=True,
                 temperature=0.1,
                 request_timeout=60.0
                )

Settings.llm =llm

ollama_embedding = OllamaEmbedding(
    # model_name="dztech/bge-large-zh:v1.5",
    # model_name="bge-m3:latest",
    model_name="chatfire/bge-m3:q8_0",
    base_url="http://192.168.0.72:11435",
    ollama_additional_kwargs={"mirostat": 0}, # -mirostat N 使用 Mirostat 采样。
)

Settings.embed_model = ollama_embedding