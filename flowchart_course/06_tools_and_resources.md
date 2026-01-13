# Tools and Resources

While you can always draw flowcharts by hand, using software can make it easier to create, edit, and share them professionally.

## Software and Online Tools

- **diagrams.net** (formerly draw.io):
  - **Pros:** Free, open-source, powerful. Can be used online or as a desktop app. Integrates with Google Drive, Confluence, etc.
  - **Cons:** The interface can be slightly less polished than paid competitors.

- **Lucidchart:**
  - **Pros:** Very intuitive and user-friendly. Excellent for collaboration. Wide range of templates.
  - **Cons:** The free tier is limited in the number of documents and objects per document.

- **Microsoft Visio:**
  - **Pros:** The industry standard for professional diagramming. Tightly integrated with the Microsoft Office suite.
  - **Cons:** Can be expensive. Only available for Windows.

- **Miro:**
  - **Pros:** An infinite online whiteboard that is great for brainstorming and collaborative flowcharting.
  - **Cons:** Less focused on pure diagramming than other tools.

## Text-based Diagramming

For developers, text-based tools allow you to create diagrams using code-like syntax.

- **Mermaid JS:**
  - Lets you create diagrams using Markdown-like text. It is supported in many platforms, including GitHub and GitLab.
  - **Example:**
    ```mermaid
    graph TD;
        A[Start] --> B{Is it raining?};
        B -- Yes --> C[Take umbrella];
        B -- No --> D[Enjoy the sun];
        C --> E[End];
        D --> E;
    ```
