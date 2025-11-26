import chromadb
import uuid

delimiter = ","
client = chromadb.Client()

collection = client.get_or_create_collection(name="products")

with open("products.txt", "r", encoding="utf-8") as f:
    products: list[str] = f.read().split(delimiter)
    
collection.add(
    ids=[str(uuid.uuid4()) for _ in products],
    documents=products,
    metadatas=[{"line":line} for line in range(len(products))]
)

print(collection.peek())


results = collection.query(
    query_texts=[
        "Meat"
    ],
    n_results=2
)

for i,query_results in enumerate(results["documents"]):
    print(f"\nQuery {i}")
    print("\n".join(query_results))