from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")

def save_note(note):
    if not os.path.exists(note_file):
        with open(note_file, "w") as f:
            f.write(note)
    
    with open(note_file, "a") as f:
        content = f"\n{note}"
        f.write(content)
        
    return "note saved"

note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="This tool can save text based note to a file for the user"
)
