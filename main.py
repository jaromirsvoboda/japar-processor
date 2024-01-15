from japar_processor.japar_processor import JaparProcessor
import sys

if __name__ == "__main__":
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    app = JaparProcessor(file_path)
    app.run()
