import inspect
import math
import random
import re
import string
import textwrap
from datetime import date
from pathlib import Path
from typing import Any, Dict, List

import streamlit as st


# ---------------------------
# Custom function library
# ---------------------------
def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def is_prime(n: int) -> bool:
    """Return True when n is a prime number."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")
    if n < 2:
        raise ValueError("n must be at least 2.")
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (a, b)):
        raise TypeError("Both values must be integers.")
    if a == 0 and b == 0:
        raise ValueError("Both values cannot be zero.")
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers."""
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (a, b)):
        raise TypeError("Both values must be integers.")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def reverse_text(text: str) -> str:
    """Reverse a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Check whether a string reads the same forwards and backwards."""
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    normalized = "".join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]


def count_vowels(text: str) -> int:
    """Count vowels in a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)


def word_count(text: str) -> int:
    """Count words in a string."""
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    return len(re.findall(r"\b\w+\b", text))


def remove_duplicates(values: List[Any]) -> List[Any]:
    """Remove duplicates while keeping the original order."""
    if not isinstance(values, list):
        raise TypeError("values must be a list.")
    seen = set()
    result = []
    for item in values:
        key = (item, type(item))
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def second_largest(values: List[int]) -> int | None:
    """Return the second largest unique number in a list."""
    if not isinstance(values, list):
        raise TypeError("values must be a list.")
    if len(values) < 2:
        raise ValueError("Provide at least two numbers.")
    if not all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in values):
        raise TypeError("All values must be numeric.")
    unique_values = sorted(set(values), reverse=True)
    if len(unique_values) < 2:
        return None
    return unique_values[1]


def maximum(values: List[int]) -> int | float:
    """Return the largest number in a list."""
    if not isinstance(values, list):
        raise TypeError("values must be a list.")
    if not values:
        raise ValueError("values cannot be empty.")
    if not all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in values):
        raise TypeError("All values must be numeric.")
    return max(values)


def average(values: List[int]) -> float:
    """Return the average of a list of numbers."""
    if not isinstance(values, list):
        raise TypeError("values must be a list.")
    if not values:
        raise ValueError("values cannot be empty.")
    if not all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in values):
        raise TypeError("All values must be numeric.")
    return sum(values) / len(values)


def read_file(path: str) -> str:
    """Read the contents of a file."""
    if not isinstance(path, str) or not path.strip():
        raise ValueError("Provide a file path.")
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return file_path.read_text(encoding="utf-8")


def count_lines(path: str) -> int:
    """Count the number of lines in a text file."""
    return len(read_file(path).splitlines())


def count_words(path: str) -> int:
    """Count the number of words in a text file."""
    return len(re.findall(r"\b\w+\b", read_file(path)))


def file_extension(path: str) -> str:
    """Return the file extension of a path."""
    if not isinstance(path, str) or not path.strip():
        raise ValueError("Provide a file path.")
    return Path(path).suffix.lower()


def password_generator(length: int, include_symbols: bool = True) -> str:
    """Generate a random password."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("length must be an integer.")
    if length < 4:
        raise ValueError("length must be at least 4.")
    alphabet = string.ascii_letters + string.digits
    if include_symbols:
        alphabet += string.punctuation
    return "".join(random.choice(alphabet) for _ in range(length))


def bmi_calculator(weight_kg: float, height_m: float) -> float:
    """Calculate the BMI from weight in kilograms and height in meters."""
    if not all(isinstance(value, (int, float)) and not isinstance(value, bool) for value in (weight_kg, height_m)):
        raise TypeError("weight and height must be numbers.")
    if height_m <= 0 or weight_kg <= 0:
        raise ValueError("height and weight must be positive.")
    return round(weight_kg / (height_m * height_m), 2)


def age_calculator(birth_year: int) -> int:
    """Calculate age based on the current year."""
    if not isinstance(birth_year, int) or isinstance(birth_year, bool):
        raise TypeError("birth_year must be an integer.")
    if birth_year < 1900 or birth_year > date.today().year:
        raise ValueError("birth_year is out of range.")
    return date.today().year - birth_year


def random_number(start: int, end: int) -> int:
    """Return a random integer between two values."""
    if not all(isinstance(value, int) and not isinstance(value, bool) for value in (start, end)):
        raise TypeError("start and end must be integers.")
    if start > end:
        raise ValueError("start must be less than or equal to end.")
    return random.randint(start, end)


# ---------------------------
# Metadata for the UI
# ---------------------------
FUNCTIONS: List[Dict[str, Any]] = [
    {
        "name": "factorial",
        "display_name": "Factorial",
        "category": "Math",
        "keywords": ["math", "number", "factorial", "multiply"],
        "description": "Compute the factorial of a non-negative integer.",
        "parameters": [{"name": "n", "label": "Number", "type": "int", "default": 5, "help": "Enter a non-negative integer."}],
        "returns": "An integer representing n!.",
        "func": factorial,
    },
    {
        "name": "is_prime",
        "display_name": "Prime Checker",
        "category": "Math",
        "keywords": ["prime", "number", "check"],
        "description": "Determine whether a value is prime.",
        "parameters": [{"name": "n", "label": "Number", "type": "int", "default": 17, "help": "Use a whole number of at least 2."}],
        "returns": "True or False.",
        "func": is_prime,
    },
    {
        "name": "gcd",
        "display_name": "GCD",
        "category": "Math",
        "keywords": ["gcd", "greatest", "common", "divisor"],
        "description": "Find the greatest common divisor of two integers.",
        "parameters": [
            {"name": "a", "label": "First number", "type": "int", "default": 48},
            {"name": "b", "label": "Second number", "type": "int", "default": 18},
        ],
        "returns": "The greatest common divisor.",
        "func": gcd,
    },
    {
        "name": "lcm",
        "display_name": "LCM",
        "category": "Math",
        "keywords": ["lcm", "least", "common", "multiple"],
        "description": "Find the least common multiple of two integers.",
        "parameters": [
            {"name": "a", "label": "First number", "type": "int", "default": 12},
            {"name": "b", "label": "Second number", "type": "int", "default": 18},
        ],
        "returns": "The least common multiple.",
        "func": lcm,
    },
    {
        "name": "reverse_text",
        "display_name": "Reverse",
        "category": "Strings",
        "keywords": ["string", "reverse", "text"],
        "description": "Reverse the characters in a string.",
        "parameters": [{"name": "text", "label": "Text", "type": "text", "default": "streamlit"}],
        "returns": "The reversed string.",
        "func": reverse_text,
    },
    {
        "name": "is_palindrome",
        "display_name": "Palindrome",
        "category": "Strings",
        "keywords": ["palindrome", "string", "text"],
        "description": "Check whether a string is a palindrome.",
        "parameters": [{"name": "text", "label": "Text", "type": "text", "default": "racecar"}],
        "returns": "True or False.",
        "func": is_palindrome,
    },
    {
        "name": "count_vowels",
        "display_name": "Count Vowels",
        "category": "Strings",
        "keywords": ["vowels", "string", "letters"],
        "description": "Count vowels in a string.",
        "parameters": [{"name": "text", "label": "Text", "type": "text", "default": "hello world"}],
        "returns": "The number of vowels.",
        "func": count_vowels,
    },
    {
        "name": "word_count",
        "display_name": "Word Counter",
        "category": "Strings",
        "keywords": ["words", "count", "text"],
        "description": "Count the words in a string.",
        "parameters": [{"name": "text", "label": "Text", "type": "text", "default": "Python mini library"}],
        "returns": "The number of words.",
        "func": word_count,
    },
    {
        "name": "remove_duplicates",
        "display_name": "Remove Duplicates",
        "category": "Lists",
        "keywords": ["list", "duplicates", "unique"],
        "description": "Remove repeated values while keeping order.",
        "parameters": [{"name": "values", "label": "Items (comma-separated)", "type": "list_text", "default": "one,two,one,three"}],
        "returns": "A list with duplicates removed.",
        "func": remove_duplicates,
    },
    {
        "name": "second_largest",
        "display_name": "Second Largest",
        "category": "Lists",
        "keywords": ["list", "largest", "second"],
        "description": "Return the second largest unique number from a list.",
        "parameters": [{"name": "values", "label": "Numbers (comma-separated)", "type": "list_int", "default": "10,4,8,2"}],
        "returns": "The second largest unique value or None.",
        "func": second_largest,
    },
    {
        "name": "maximum",
        "display_name": "Maximum",
        "category": "Lists",
        "keywords": ["largest", "list", "max"],
        "description": "Find the largest value in a list.",
        "parameters": [{"name": "values", "label": "Numbers (comma-separated)", "type": "list_int", "default": "4,9,1,12"}],
        "returns": "The maximum value.",
        "func": maximum,
    },
    {
        "name": "average",
        "display_name": "Average",
        "category": "Lists",
        "keywords": ["average", "mean", "list"],
        "description": "Find the average of a list of numbers.",
        "parameters": [{"name": "values", "label": "Numbers (comma-separated)", "type": "list_int", "default": "2,4,6"}],
        "returns": "The average as a float.",
        "func": average,
    },
    {
        "name": "read_file",
        "display_name": "Read File",
        "category": "Files",
        "keywords": ["file", "read", "text"],
        "description": "Read the contents of a text file.",
        "parameters": [{"name": "path", "label": "File path", "type": "file_path", "default": "README.md"}],
        "returns": "The file content as a string.",
        "func": read_file,
    },
    {
        "name": "count_lines",
        "display_name": "Count Lines",
        "category": "Files",
        "keywords": ["file", "lines", "count"],
        "description": "Count the lines in a text file.",
        "parameters": [{"name": "path", "label": "File path", "type": "file_path", "default": "README.md"}],
        "returns": "The number of lines.",
        "func": count_lines,
    },
    {
        "name": "count_words",
        "display_name": "Count Words",
        "category": "Files",
        "keywords": ["file", "words", "count"],
        "description": "Count the words in a text file.",
        "parameters": [{"name": "path", "label": "File path", "type": "file_path", "default": "README.md"}],
        "returns": "The number of words.",
        "func": count_words,
    },
    {
        "name": "file_extension",
        "display_name": "File Extension",
        "category": "Files",
        "keywords": ["file", "extension", "type"],
        "description": "Return the suffix of a file path.",
        "parameters": [{"name": "path", "label": "File path", "type": "file_path", "default": "example.py"}],
        "returns": "The file extension as a string.",
        "func": file_extension,
    },
    {
        "name": "password_generator",
        "display_name": "Password Generator",
        "category": "Utilities",
        "keywords": ["password", "security", "random"],
        "description": "Generate a random password of the requested length.",
        "parameters": [
            {"name": "length", "label": "Length", "type": "int", "default": 12},
            {"name": "include_symbols", "label": "Include symbols", "type": "bool", "default": True},
        ],
        "returns": "A generated password string.",
        "func": password_generator,
    },
    {
        "name": "bmi_calculator",
        "display_name": "BMI Calculator",
        "category": "Utilities",
        "keywords": ["bmi", "health", "weight"],
        "description": "Calculate BMI from weight and height.",
        "parameters": [
            {"name": "weight_kg", "label": "Weight (kg)", "type": "float", "default": 70.0},
            {"name": "height_m", "label": "Height (m)", "type": "float", "default": 1.75},
        ],
        "returns": "BMI rounded to two decimal places.",
        "func": bmi_calculator,
    },
    {
        "name": "age_calculator",
        "display_name": "Age Calculator",
        "category": "Utilities",
        "keywords": ["age", "year", "birthday"],
        "description": "Estimate age from the birth year.",
        "parameters": [{"name": "birth_year", "label": "Birth year", "type": "int", "default": 1995}],
        "returns": "The user's age in years.",
        "func": age_calculator,
    },
    {
        "name": "random_number",
        "display_name": "Random Number",
        "category": "Utilities",
        "keywords": ["random", "number", "range"],
        "description": "Generate a random integer inside a range.",
        "parameters": [
            {"name": "start", "label": "Start", "type": "int", "default": 1},
            {"name": "end", "label": "End", "type": "int", "default": 10},
        ],
        "returns": "A random integer between start and end.",
        "func": random_number,
    },
]


# ---------------------------
# UI helpers
# ---------------------------
def get_categories() -> List[str]:
    return sorted({entry["category"] for entry in FUNCTIONS})


def get_source_code(func: Any) -> str:
    return textwrap.dedent(inspect.getsource(func))


def parse_list_input(raw_value: str, value_type: str) -> List[Any]:
    if not raw_value.strip():
        return []
    if value_type == "list_int":
        pieces = [piece.strip() for piece in raw_value.split(",") if piece.strip()]
        try:
            return [int(piece) for piece in pieces]
        except ValueError as exc:
            raise ValueError("Use comma-separated integers like 1,2,3.") from exc
    if value_type == "list_text":
        return [piece.strip() for piece in raw_value.split(",") if piece.strip()]
    raise ValueError("Unsupported list format.")


def render_input_controls(parameters: List[Dict[str, Any]]) -> Dict[str, Any]:
    values: Dict[str, Any] = {}
    for param in parameters:
        name = param["name"]
        label = param.get("label", name)
        value_type = param["type"]
        default = param.get("default")
        key = f"{name}_{param['label']}"
        
        if value_type == "int":
            # Use sliders for small integer ranges (0-100)
            if name in {"length", "n"} and default and default <= 100:
                values[name] = st.slider(
                    label, 
                    min_value=0, 
                    max_value=100, 
                    value=int(default), 
                    step=1, 
                    key=key,
                    help=f"Slide to adjust {label}"
                )
            else:
                values[name] = st.number_input(label, value=int(default), step=1, key=key)
        elif value_type == "float":
            # Use sliders for floating point ranges (0-10)
            if name in {"weight_kg", "height_m"} and default:
                min_val = 0.5 if "height" in name.lower() else 20.0
                max_val = 2.5 if "height" in name.lower() else 150.0
                step_val = 0.1 if "height" in name.lower() else 1.0
                values[name] = st.slider(
                    label, 
                    min_value=min_val, 
                    max_value=max_val, 
                    value=float(default), 
                    step=step_val, 
                    key=key,
                    help=f"Slide to adjust {label}"
                )
            else:
                values[name] = st.number_input(label, value=float(default), step=0.1, key=key)
        elif value_type == "text":
            values[name] = st.text_input(label, value=str(default), key=key, placeholder="Enter text...")
        elif value_type == "bool":
            values[name] = st.checkbox(label, value=bool(default), key=key)
        elif value_type in {"list_int", "list_text"}:
            raw_value = st.text_input(label, value=str(default), key=key, placeholder="Comma-separated values...")
            values[name] = parse_list_input(raw_value, value_type)
        elif value_type == "file_path":
            values[name] = st.text_input(label, value=str(default), key=key, placeholder="Enter file path...")
        else:
            raise ValueError(f"Unsupported parameter type: {value_type}")
    return values


def run_selected_function(entry: Dict[str, Any]) -> None:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 20px; border-radius: 12px; margin-bottom: 20px;
                    box-shadow: 0 8px 32px rgba(245, 87, 108, 0.3);">
            <h2 style="color: white; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
                       font-size: 2em; letter-spacing: 0.5px;">
                {entry['display_name']}
            </h2>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<p style='color: #e0f2fe; font-weight: bold; font-size: 14px;'>📁 <span style='color: #cffafe;'>{entry['category']}</span></p>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<p style='color: #e0f2fe; font-weight: bold; font-size: 14px;'>⭐ <span style='color: #fbbf24;'>Premium</span></p>", unsafe_allow_html=True)
    with col3:
        param_count = len(entry["parameters"])
        st.markdown(f"<p style='color: #e0f2fe; font-weight: bold; font-size: 14px;'>⚙️ <span style='color: #86efac;'>{param_count} params</span></p>", unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown(f"<p style='color: #cffafe; font-size: 16px; line-height: 1.6;'>{entry['description']}</p>", unsafe_allow_html=True)

    with st.expander("📋 Function Details", expanded=False):
        st.markdown("<p style='color: #e0f2fe; font-weight: bold; margin-bottom: 10px;'>📝 Parameters</p>", unsafe_allow_html=True)
        if entry["parameters"]:
            for i, param in enumerate(entry["parameters"]):
                st.markdown(f"""
                    <div style="background: rgba(99, 102, 241, 0.1); padding: 10px; border-left: 3px solid #6366f1; 
                                border-radius: 4px; margin-bottom: 8px;">
                        <p style='color: #c7d2fe; margin: 0;'>
                            <b>{i+1}. {param['label']}</b><br/>
                            <span style='color: #a5b4fc; font-size: 13px;'>{param['help'] if 'help' in param else 'User input required'}</span>
                        </p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("✓ No parameters required for this function")

        st.markdown("<p style='color: #e0f2fe; font-weight: bold; margin-top: 15px; margin-bottom: 10px;'>✅ Return Value</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: #bae6fd; background: rgba(6, 182, 212, 0.1); padding: 10px; border-radius: 6px;'>{entry['returns']}</p>", unsafe_allow_html=True)

    with st.expander("💻 Source Code", expanded=False):
        st.code(get_source_code(entry["func"]), language="python")

    st.markdown("<h3 style='color: #e0f2fe; margin-top: 30px;'>⚙️ Configure & Execute</h3>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
            <div style="background: rgba(99, 102, 241, 0.1); padding: 15px; border-radius: 10px; 
                        border: 1px solid rgba(99, 102, 241, 0.3); margin-bottom: 15px;">
        """, unsafe_allow_html=True)
        
        values = render_input_controls(entry["parameters"])
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        if st.button(f"▶️ Execute {entry['display_name']}", key=f"run_{entry['name']}", use_container_width=True):
            with st.spinner("🔄 Processing..."):
                import time
                progress_bar = st.progress(0)
                
                try:
                    # Simulate processing with progress
                    for percent_complete in range(100):
                        progress_bar.progress(percent_complete + 1)
                        time.sleep(0.01)
                    
                    result = entry["func"](**values)
                    progress_bar.empty()
                    
                    st.success("✅ Execution completed successfully")
                    st.markdown("""
                        <div style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1) 0%, rgba(34, 197, 94, 0.05) 100%);
                                    padding: 15px; border-radius: 10px; border-left: 4px solid #22c55e;">
                    """, unsafe_allow_html=True)
                    
                    if isinstance(result, (dict, list)):
                        st.json(result)
                    else:
                        st.markdown(f"<h4 style='color: #86efac; margin: 0;'>📊 Result: <code style='background: #1e293b; padding: 5px 10px; border-radius: 4px; color: #86efac;'>{result}</code></h4>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                except Exception as exc:  # noqa: BLE001
                    progress_bar.empty()
                    st.error(f"❌ Invalid input or execution error: {exc}")
    
    with col2:
        if st.button("🔄 Reset", key=f"reset_{entry['name']}", use_container_width=True):
            st.rerun()
    
    with col3:
        if st.button("📋 Copy", key=f"copy_{entry['name']}", use_container_width=True):
            st.info("Code copied to clipboard! (Use right-click on code block to copy)")


def main() -> None:
    st.set_page_config(page_title="Python Mini Library", page_icon="📚", layout="wide", initial_sidebar_state="expanded")
    
    # Custom CSS styling with animations
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Main background gradient with animation */
        .main {
            background: linear-gradient(-45deg, #667eea, #764ba2, #f093fb, #4facfe);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e3a8a 0%, #2d5a96 100%);
        }
        
        [data-testid="stSidebar"] > div:first-child {
            background: linear-gradient(180deg, #1e3a8a 0%, #2d5a96 100%);
        }
        
        /* Header styling with fade-in animation */
        h1 {
            color: #ffffff !important;
            text-shadow: 0 0 20px rgba(6, 182, 212, 0.5);
            text-align: center;
            font-size: 3em !important;
            font-weight: 700 !important;
            animation: fadeInDown 0.8s ease-out;
            letter-spacing: 1px;
        }
        
        h2 {
            color: #ffffff !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            animation: fadeInUp 0.6s ease-out;
        }
        
        h3 {
            color: #ffffff !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
            animation: fadeInUp 0.6s ease-out;
        }
        
        /* Text styling */
        .stMarkdown {
            color: #ffffff;
        }
        
        p {
            color: #e0e7ff !important;
        }
        
        /* Button styling with enhanced animations */
        .stButton > button {
            background: linear-gradient(90deg, #06b6d4 0%, #0891b2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            padding: 12px 24px;
            box-shadow: 0 4px 15px rgba(6, 182, 212, 0.4);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button:before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .stButton > button:hover:before {
            width: 300px;
            height: 300px;
        }
        
        .stButton > button:hover {
            background: linear-gradient(90deg, #0891b2 0%, #0d9488 100%);
            box-shadow: 0 8px 25px rgba(6, 182, 212, 0.8);
            transform: translateY(-3px) scale(1.02);
        }
        
        /* Input styling with focus animations */
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border: 2px solid #06b6d4 !important;
            border-radius: 8px !important;
            color: #1e293b !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput > div > div > input:focus {
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.5) !important;
            transform: scale(1.02);
        }
        
        .stNumberInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border: 2px solid #06b6d4 !important;
            border-radius: 8px !important;
            color: #1e293b !important;
            transition: all 0.3s ease !important;
        }
        
        .stNumberInput > div > div > input:focus {
            box-shadow: 0 0 20px rgba(6, 182, 212, 0.5) !important;
        }
        
        .stSlider > div > div > div {
            background: linear-gradient(90deg, #06b6d4 0%, #0891b2 100%) !important;
        }
        
        .stSelectbox > div > div > select {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border: 2px solid #06b6d4 !important;
            border-radius: 8px !important;
            color: #1e293b !important;
            transition: all 0.3s ease !important;
        }
        
        .stCheckbox > label {
            color: #ffffff !important;
            transition: all 0.3s ease;
        }
        
        .stCheckbox > label:hover {
            text-shadow: 0 0 10px rgba(6, 182, 212, 0.5);
        }
        
        /* Expander styling */
        .streamlit-expanderHeader {
            background: linear-gradient(90deg, #8b5cf6 0%, #6366f1 100%) !important;
            color: white !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
        }
        
        .streamlit-expanderHeader:hover {
            box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
            transform: translateX(5px);
        }
        
        /* Success, error, warning messages */
        .stSuccess {
            background-color: rgba(34, 197, 94, 0.2) !important;
            color: #86efac !important;
            border: 2px solid #22c55e !important;
            border-radius: 8px !important;
            animation: slideInRight 0.5s ease-out;
        }
        
        .stError {
            background-color: rgba(239, 68, 68, 0.2) !important;
            color: #fca5a5 !important;
            border: 2px solid #ef4444 !important;
            border-radius: 8px !important;
            animation: slideInRight 0.5s ease-out;
        }
        
        .stWarning {
            background-color: rgba(245, 158, 11, 0.2) !important;
            color: #fcd34d !important;
            border: 2px solid #f59e0b !important;
            border-radius: 8px !important;
            animation: slideInRight 0.5s ease-out;
        }
        
        /* Code styling */
        .stCodeBlock {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%) !important;
            border: 2px solid #475569 !important;
            border-radius: 8px !important;
            animation: fadeIn 0.5s ease-out;
        }
        
        /* Column styling */
        [data-testid="column"] {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            animation: scaleInUp 0.6s ease-out;
        }
        
        /* Sidebar text */
        [data-testid="stSidebar"] h2 {
            color: #e0f2fe !important;
        }
        
        [data-testid="stSidebar"] p {
            color: #bae6fd !important;
        }
        
        /* Link styling */
        a {
            color: #00d4ff !important;
            transition: all 0.3s ease;
        }
        
        a:hover {
            color: #00f0ff !important;
            text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
        }
        
        /* Animation definitions */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(-30px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        @keyframes scaleInUp {
            from {
                opacity: 0;
                transform: scale(0.95) translateY(20px);
            }
            to {
                opacity: 1;
                transform: scale(1) translateY(0);
            }
        }
        
        @keyframes pulse {
            0%, 100% {
                box-shadow: 0 4px 15px rgba(6, 182, 212, 0.4);
            }
            50% {
                box-shadow: 0 4px 25px rgba(6, 182, 212, 0.8);
            }
        }
        
        /* Professional card styling */
        .function-card {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 20px;
            backdrop-filter: blur(10px);
            transition: all 0.4s ease;
        }
        
        .function-card:hover {
            background: rgba(255, 255, 255, 0.12);
            border-color: rgba(6, 182, 212, 0.5);
            box-shadow: 0 8px 32px rgba(6, 182, 212, 0.2);
            transform: translateY(-5px);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🚀 Python Mini Library")
    st.caption("✨ Search, explore, and run custom Python functions from a professional, interactive library")

    with st.sidebar:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 30px; animation: fadeInDown 1s ease-out;">
                <h1 style="color: #e0f2fe; font-size: 2.5em; margin: 0; text-shadow: 0 0 20px rgba(6, 182, 212, 0.5);">🔍</h1>
                <h2 style="color: #e0f2fe; margin-top: 10px; letter-spacing: 1px;">Library Control</h2>
                <p style="color: #bae6fd; margin-top: 5px; font-size: 12px;">Manage & Execute Functions</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='color: #bae6fd; font-weight: bold; margin-top: 10px; margin-bottom: 5px;'>🔎 Search Functions</p>", unsafe_allow_html=True)
        search_query = st.text_input(
            "Search by name or keyword", 
            placeholder="e.g., factorial, prime, reverse...",
            label_visibility="collapsed",
            help="Type to search for functions"
        )
        
        st.markdown("<p style='color: #bae6fd; font-weight: bold; margin-top: 20px; margin-bottom: 5px;'>🏷️ Filter by Category</p>", unsafe_allow_html=True)
        category_filter = st.selectbox(
            "Select a category", 
            ["All", *get_categories()], 
            label_visibility="collapsed",
            help="Filter functions by category"
        )
        
        st.divider()
        
        st.markdown("""
            <p style='color: #a5b4fc; font-size: 12px; text-align: center; margin-top: 20px;'>
                📊 Python Mini Library v1.0<br/>
                Built with ❤️ using Streamlit
            </p>
        """, unsafe_allow_html=True)

    filtered_functions = [
        entry
        for entry in FUNCTIONS
        if (category_filter == "All" or entry["category"] == category_filter)
        and (
            search_query.lower() in entry["name"].lower()
            or search_query.lower() in entry["display_name"].lower()
            or any(search_query.lower() in keyword.lower() for keyword in entry.get("keywords", []))
        )
    ]

    if not filtered_functions:
        st.warning("No functions matched your search. Try another keyword or category.")
        return

    left_col, right_col = st.columns([0.9, 2.1])
    with left_col:
        func_count = len(filtered_functions)
        plural = "s" if func_count != 1 else ""
        st.markdown(f"""
            <div style="background: linear-gradient(180deg, #667eea 0%, #764ba2 100%); 
                        padding: 20px; border-radius: 12px; margin-bottom: 20px;
                        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);">
                <h3 style="color: white; text-align: center; margin: 0; letter-spacing: 0.5px;">📚 Function Catalog</h3>
                <p style="color: #e0f2fe; text-align: center; margin: 5px 0 0 0; font-size: 12px;">
                    {func_count} function{plural} available
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        for i, entry in enumerate(filtered_functions):
            # Color palette for function buttons
            colors = [
                ("linear-gradient(135deg, #f093fb 0%, #f5576c 100%)", "#fff"),
                ("linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)", "#fff"),
                ("linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)", "#fff"),
                ("linear-gradient(135deg, #fa709a 0%, #fee140 100%)", "#1a202c"),
                ("linear-gradient(135deg, #30cfd0 0%, #330867 100%)", "#fff"),
            ]
            gradient, text_color = colors[i % len(colors)]
            
            st.markdown(f"""
                <div style="background: {gradient}; border-radius: 8px; padding: 2px; margin-bottom: 8px;">
                    <div style="background: rgba(0,0,0,0.1); border-radius: 6px; padding: 0; overflow: hidden;">
            """, unsafe_allow_html=True)
            
            if st.button(
                f"🔹 {entry['display_name']}", 
                key=f"select_{entry['name']}", 
                use_container_width=True,
                help=entry['description']
            ):
                st.session_state["selected_function"] = entry["name"]
            
            st.markdown("</div></div>", unsafe_allow_html=True)

    with right_col:
        st.markdown("""
            <div style="background: rgba(99, 102, 241, 0.08); 
                        padding: 30px; border-radius: 16px; border: 1px solid rgba(99, 102, 241, 0.3); 
                        backdrop-filter: blur(10px); animation: scaleInUp 0.6s ease-out;">
        """, unsafe_allow_html=True)
        
        selected_name = st.session_state.get("selected_function")
        selected_entry = next((entry for entry in filtered_functions if entry["name"] == selected_name), filtered_functions[0])
        run_selected_function(selected_entry)
        
        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
