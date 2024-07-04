from groq import Groq
import os
import json

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)

def generate_book_content(title):
    prompt = f"Generate a detailed outline for a book titled '{title}'. Include chapter titles and brief descriptions for each chapter."
    
    completion = groq_client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are an expert book outliner. Create a detailed book outline with chapters and brief descriptions."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        stream=False,
        stop=None,
    )

    outline = completion.choices[0].message.content
    chapters = outline.split('\n\n')
    
    book_content = {}
    for chapter in chapters:
        if ':' in chapter:
            chapter_title, chapter_description = chapter.split(':', 1)
            book_content[chapter_title.strip()] = chapter_description.strip()

    return book_content
