import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

def check_similarity(doc1, doc2):
    """
    This function takes two text documents as input, processes them with spaCy's NLP model, 
    and returns a similarity score between 0 and 1.
    """
    # Process the documents
    doc1_nlp = nlp(doc1)
    doc2_nlp = nlp(doc2)
    
    # Calculate similarity score
    similarity_score = doc1_nlp.similarity(doc2_nlp)
    
    return similarity_score

# Sample texts (You can replace these with actual file reads)
document1 = """Natural Language Processing is a field of artificial intelligence that deals with the interaction between computers and humans using the natural language."""
document2 = """Natural language processing (NLP) is a subfield of AI that focuses on the interaction between computers and human language."""

# Check for similarity
similarity = check_similarity(document1, document2)

print(f"Similarity Score: {similarity:.2f}")

if similarity > 0.8:
    print("The documents are very similar, possible plagiarism!")
else:
    print("The documents are not significantly similar.")
