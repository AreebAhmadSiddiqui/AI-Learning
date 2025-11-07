# Text Splitting

- Bade text ko chote chunks mein convert karna is text splitting

![text-splitting](text-splitting.png)

### Why do this?

- Isliye kiya jata taki LLM ki output ki quality improve ho jae
- Context length exceed kar sakta hai are poora text content ek saath dal diya
- Ex - Tumhara context length is 50 tokens lekin tumne use 100 se zyada tokens wala text de diya ab LLM chalega hi


`Text splitting `is the process of breaking down a large document or piece of text into smaller, semantically meaningful segments (called "`chunks`") before processing them with an LLM.

Think of it like this: You have a 300-page book, but you can only feed the LLM a few pages at a time. Text splitting is how you decide which few pages to send.

### Why is it Needed? The Core Problem: Context Window
LLMs have a fundamental limitation called a context window. This is the maximum number of tokens (pieces of words) the model can process in a single request. It's like the model's "working memory."

|Example| Context Windows:|
|----|-------|
GPT-3.5-turbo:| ~16,000 tokens
GPT-4: |~8,000 to 128,000 tokens, depending on the version.
Claude 3:| ~200,000 tokens.

- If your document is longer than this limit, you cannot process it all at once. Text splitting is the essential strategy to work around this limitation.

### Key Reasons for Text Splitting:

- **To Fit Documents into the Context Window:** This is the primary and most obvious reason. You simply can't process a long document otherwise.

- **For Retrieval-Augmented Generation (RAG):** This is the most important modern use case. In a RAG system, you split your documents (e.g., a company knowledge base) and store the chunks in a vector database. When a user asks a question, you:

    - Search the database for the chunks most semantically similar to the question.

    - Inject only those relevant chunks into the LLM's prompt to answer the question.

    - Without splitting, you'd have to search the entire, massive document, which is inefficient and would likely exceed the context window when you try to provide the context.

- **Improved Accuracy and Focus:** Smaller, focused chunks allow the LLM to concentrate on a specific piece of information without getting distracted by irrelevant parts of a larger document. This often leads to better, more precise answers.

- **Managing Costs and Speed:** Processing smaller chunks is generally faster and cheaper than repeatedly sending a massive text block, especially if the operation needs to be done multiple times (as in RAG).

## Types of Splitting

### 1. Length Based Text Splitting

- This is the most naive approach. You simply split the text after every X characters.
- How it works: It doesn't care about words or sentences. It just counts characters.
- Pros: Extremely simple and fast.
- Cons: It often breaks words and sentences in the middle, creating chunks that are nonsensical and hard for the LLM to understand.

```python

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

```

### Chunk over lap is very important

### What is Chunk Overlap?
- Chunk overlap is the technique of having the end of one text chunk contain a small portion of the beginning of the next chunk. It's a sliding window that ensures no information is lost at the boundaries where the text is split.

- Think of it like panning a camera across a wide landscape with a narrow lens. You don't take discrete, separate photos; you take overlapping photos so you can seamlessly stitch the panorama together later.

### Why is it Needed? The "Context Loss" Problem

- The primary problem chunk overlap solves is loss of context at chunk boundaries.
- When you split text, you often break sentences, paragraphs, or ideas in half. If a chunk ends abruptly and the next chunk starts fresh, the LLM loses the context needed to understand either piece fully.

### Example Without Overlap:

- Imagine you are splitting this text with a focus on sentences:

- Original Text: "The project's success was largely due to the new agile methodology we implemented. This approach allowed for rapid iteration and continuous feedback. As a result, we delivered the product two weeks ahead of schedule."

    - Chunk 1: "The project's success was largely due to the new agile methodology we implemented."

    - Chunk 2: "As a result, we delivered the product two weeks ahead of schedule."

- The Problem: Chunk 2, "As a result...", is completely disconnected from its cause. The LLM has no idea what resulted in the early delivery. The key explanatory sentence ("This approach allowed for...") was lost at the boundary.

- Example With Overlap:

- Now, let's split the same text with an overlap of one sentence.

    - Chunk 1: "The project's success was largely due to the new agile methodology we implemented. **This approach allowed for rapid iteration and continuous feedback.**"

    - Chunk 2: "**This approach allowed for rapid iteration and continuous feedback.** As a result, we delivered the product two weeks ahead of schedule."

- The Solution: Now, both chunks are self-contained and make sense.

    - Chunk 1 has the cause and the explanation.

    - Chunk 2 has the explanation and the result.

- The overlapping sentence ("This approach...") acts as a bridge, preserving the logical flow for the LLM.


### Best for RAG is chunk overlap is 10-20% of chunk size

## 2. Recursive Character Text Splitting

### Recursive Character Text Splitting

- Ye recursively bas todta jata hai separators ke basis pe
- Bahut koshish karta hai ki character tk split karne ki naubat na ae
- Recursive Character Text Splitting is a hierarchical splitting method that attempts to keep semantically related content together by trying different separators in sequence until chunks are of the desired size.

#### How It Works

- The splitter uses a prioritized list of separators and works through them recursively:

### Default Separator Hierarchy:

"\n\n" - Double newlines (paragraphs)

"\n" - Single newlines

". " - Sentences

" " - Words

"" - Characters (fallback)

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)

# Sample text to split
sample_text = """
Artificial Intelligence (AI) is transforming modern society in profound ways.

Machine learning algorithms can now recognize patterns in data that were previously invisible to human analysts. This capability is revolutionizing fields from healthcare to finance.

In healthcare, AI systems help doctors diagnose diseases more accurately. They analyze medical images, patient records, and genetic information to identify potential health risks early.

The ethical implications of AI are equally important. We must consider privacy concerns, algorithmic bias, and the impact on employment as these technologies become more widespread.

Despite these challenges, the potential benefits of AI are enormous. It promises to solve complex problems and improve quality of life for people around the world.
"""

# Split the text
chunks = text_splitter.split_text(sample_text)

# Display results
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1} ({len(chunk)} chars):")
    print(chunk)
    print("-" * 50)

```

#### Step-by-Step Splitting Process

- Input Text Analysis
- Total characters: ~750 characters
- Target chunk size: 300 characters
- Overlap: 50 characters

Hierarchical Splitting Process
Step 1: Try "\n\n" (Paragraphs)

```
text
Chunk A: "Artificial Intelligence (AI) is transforming..." (120 chars) ✓
Chunk B: "Machine learning algorithms can now..." (150 chars) ✓
Chunk C: "In healthcare, AI systems help..." (130 chars) ✓
Chunk D: "The ethical implications of AI..." (180 chars) ✓
Chunk E: "Despite these challenges, the potential..." (150 chars) ✓
All chunks are under 300 characters → Process complete

Resulting Chunks
Chunk 1
text
Artificial Intelligence (AI) is transforming modern society in profound ways.
Chunk 2
text
Machine learning algorithms can now recognize patterns in data that were previously invisible to human analysts. This capability is revolutionizing fields from healthcare to finance.
Chunk 3
text
In healthcare, AI systems help doctors diagnose diseases more accurately. They analyze medical images, patient records, and genetic information to identify potential health risks early.
Chunk 4
text
The ethical implications of AI are equally important. We must consider privacy concerns, algorithmic bias, and the impact on employment as these technologies become more widespread.
Chunk 5
text
Despite these challenges, the potential benefits of AI are enormous. It promises to solve complex problems and improve quality of life for people around the world.
Alternative Scenario: Larger Text
If the text had been longer and paragraphs exceeded 300 characters, the splitter would continue down the separator hierarchy:
```
Example with longer paragraphs:

```python
# If a paragraph is too large, it moves to the next separator
long_paragraph = "This is a very long paragraph. " * 20  # ~600 chars

# Process:
# 1. Try "\n\n" - No separation found
# 2. Try "\n" - No separation found  
# 3. Try ". " - Split into sentences
# 4. Combine sentences until ~300 chars

```
Key Parameters

|Parameter|	Description	Recommended Value|
|--|--|
chunk_size	|Maximum size of each chunk	500-1500 characters
chunk_overlap|	Overlap between chunks	10-20% of chunk_size
separators	|Split hierarchy	["\n\n", "\n", ". ", " ", ""]


## 3. Document Splitting

- Ye wo files ko change karta hai jo pure text ni hai
- Code wagerah hai
- Recursive hi use karte hai bas separators alag ho jate hai

### Text & Documents
|Data Type	|Separators Hierarchy|
|--|--|
General Text	|["\n\n", "\n", ". ", "! ", "? ", " ", ""]
Markdown	|["\n# ", "\n## ", "\n### ", "\n#### ", "\n- ", "\n* ", "\n\n", "\n", " "]
LaTeX	|["\n\\chapter{", "\n\\section{", "\n\\subsection{", "\n\\begin{", "\n\n", "\n", " "]
HTML	|[">\n\n<", ">\n<", "><", "\n\n", "\n", " "]

### Programming Languages
|Language	|Separators Hierarchy|
|--|--|
Python|	["\n\nclass ", "\n\ndef ", "\n\nasync def ", "\n\nif ", "\n\nfor ", "\n\n", "\n", " "]
JavaScript|	["\n\nclass ", "\n\nfunction ", "\n\nconst ", "\n\nlet ", "\n\nif ", "\n\nfor ", "\n\n", "\n", " "]
Java|	["\n\nclass ", "\n\npublic ", "\n\nprivate ", "\n\nprotected ", "\n\nif ", "\n\nfor ", "\n\n", "\n", " "]
SQL|	["\n\nCREATE ", "\n\nSELECT ", "\n\nINSERT ", "\n\nUPDATE ", "\n\nWHERE ", "\n\n", "\n", " "]
CSS	|["\n\n}", "\n}", " {", "; ", " "]

### Structured Data
Format|	Separators Hierarchy|
|--|--|
JSON|	[",\n\n", ",\n", ", ", ""]
XML	|[">\n\n<", ">\n<", "><", ""]
YAML|	["\n\n", "\n---", "\n- ", "\n", ": ", " "]
CSV/TSV|	["\n\n", "\n", "\t", ", ", " "]

### Specialized Formats
|Format|	Separators Hierarchy|
|--|--|
Configuration| Files	["\n\n[", "\n\n", "\n", "= ", " "]
Log Files|	["\n\n", "\n", " - ", " "]
Academic Papers	|["\n\n## ", "\n\n", "\n", ". ", " "]
Technical Documentation|	["\n\n# ", "\n\n## ", "\n\n- ", "\n\n", "\n", ". ", " "]


### Notes:
- **Order Matters:** Separators are tried from first to last
- **Size Control:** Splitting continues until chunks are under target size
- **Overlap:** Typically 10-20% of chunk size maintains context
- **Customization:** Adjust based on your specific data structure and use case

## 4. Semantic Meaning Based

- Meaning ko extract karke diffrent meaning ka different chunk
- 