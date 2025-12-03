"""
CLI entry point for the Gemini CLI Application (Chat + Summarizer).

Usage:
    python main.py

This app provides:
- Chat mode: Ask a question and see Gemini's response.
- Summarization mode: Paste multi-line text and get a short summary.

The app uses the official google-genai SDK and the "gemini-1.5-flash" model.
"""
from typing import List

from gemini_client import ask_gemini, summarize_text


def show_menu() -> None:
    print("=" * 36)
    print("        Gemini CLI Application")
    print("=" * 36)
    print("1. Chat mode (ask a question)")
    print("2. Summarization mode")
    print("3. Exit")
    print("=" * 36)


def run_chat_mode() -> None:
    prompt = input("Enter your prompt: ").strip()
    if not prompt:
        print("Please enter a non-empty prompt. Returning to menu.\n")
        return
    try:
        response_text = ask_gemini(prompt)
        print("\n--- Gemini Response ---")
        print(response_text)
        print("------------------------\n")
    except Exception as e:
        print(f"An error occurred while contacting Gemini: {e}\n")


def run_summarization_mode() -> None:
    print("Paste your text below. Press Enter on an empty line to finish.")
    print("(Your text can span multiple lines.)\n")

    lines: List[str] = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    if not lines:
        print("No text entered. Returning to menu.\n")
        return

    long_text = "\n".join(lines)
    try:
        summary = summarize_text(long_text)
        print("\n--- Summary from Gemini ---")
        print(summary)
        print("---------------------------\n")
    except Exception as e:
        print(f"An error occurred while summarizing with Gemini: {e}\n")


def main() -> None:
    while True:
        show_menu()
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            run_chat_mode()
        elif choice == "2":
            run_summarization_mode()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
