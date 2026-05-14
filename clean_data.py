import ipywidgets as widgets
import importlib.util
import re
import inspect

# --- DYNAMIC DEPENDENCY MANAGEMENT ---
# This block handles environment-specific imports. We use 'find_spec' to detect
# if we are in Google Colab (Cloud) or a local Jupyter environment.
using_google_colab = importlib.util.find_spec("google.colab")
if using_google_colab:
    import google.colab.files

from IPython.display import display, clear_output
from pathlib import Path

class CleanData:
    """
    The CleanData class acts as a 'Command Center' for data workflows.
    It encapsulates file path management, environment detection, and
    cleaning logic orchestration into a single, modular unit.
    """
    def __init__(self, filetype=["Input", "Output"]):
        """
        CONSTRUCTOR: Initializes the state of the data object.
        Automatically triggers the environment-specific GUI for file selection.
        """
        # --- 1. ENCAPSULATION (Data Privacy) ---
        # We use double underscores (__) to keep these attributes private.
        # This prevents external scripts from accidentally corrupting our file lists.
        self.__input_filenames = []
        self.__output_filenames = []
        self.data_frame = None

        # --- 2. CHECK THE FILE TYPE ---
        if isinstance(filetype, str):
            filetype = [filetype]
        elif isinstance(filetype, list):
            if not all(isinstance(f, str) for f in filetype):
                raise TypeError("List elements must be all strings. Mixed types are not supported.")
        else:
            raise TypeError("Unsupported filetype parameter. Must be a string or list of strings.")

        # --- 3. AUTOMATED INITIALIZATION ---
        # We loop through the given roles (Input/Output) 
        # to gather all necessary paths
        # before any data processing begins.
        for f in sorted(list(set([ftype.lower() for ftype in filetype]))):
            self.import_files(f)
    
    def __setattr__(self, name, value):

        # Compute the PrivateClass parameters
        calling_function = inspect.stack()[1].function
        access_name = name
        public_properties = "data_frame"
        class_name = CleanData
        
        # Apply the correct private property assignment
        if PrivateClass.check_valid_property_assignment(calling_function, access_name, public_properties, class_name):       
            # Bypass custom logic and set attribute normally
            object.__setattr__(self, name, value)
        else:
            # Block all private external assignments
            raise AttributeError(f"Attribute '{name}' is read-only.")
    
    def import_files(self, filetype):
        """
        STRATEGY SELECTOR: Detects the runtime environment and launches
        the appropriate GUI logic (Colab Cloud vs. Local Desktop).
        """
        
        # --- ENVIRONMENT-BASED BRANCHING ---
        if using_google_colab:
            self.__import_files_google_colab(filetype)
        else:
            self.__import_files_jupyter_notebook(filetype)

    def __import_files_google_colab(self, filetype):
        """
        PRIVATE METHOD: Handles Google Drive pathing.
        Restricted to manual input to ensure valid /content/drive/ paths.
        """

        # Compute the PrivateClass parameters
        calling_function = inspect.stack()[1].function
        method_name = "_CleanData__import_files_google_colab"
        class_name = CleanData

        # GATEKEEPING (Security intact)
        PrivateClass.check_valid_method_access(calling_function, method_name, class_name)

        # USER GUIDANCE: help the user remember the Colab drive syntax
        path_input = widgets.Text(
            placeholder=r"Example: /content/drive/MyDrive/input.csv or G:\Drive\My Drive\input.csv",
            description="Drive Path:",
            style={"description_width": "initial"},
            layout=widgets.Layout(width='80%')
        )

        # DYNAMIC VALIDATION & ROUTING: Gatekeeping the input before adding to the manifest
        filetype, target_filenames = self.__validate_filetype(filetype, self.__input_filenames, self.__output_filenames)
        
        # DEFINE THE WIDGETS
        header = widgets.HTML(f"<h2>Select {filetype} Files</h2>")
        add_button = widgets.Button(description=f"Add {filetype} File", button_style='success', icon='plus')
        finish_button = widgets.Button(description="Lock Selection", button_style='info', icon='check')
        output_log = widgets.Output()

        def on_add_clicked(b):
            with output_log:
                # SANITIZATION: We call the static 'fix_filenames' to clean up user input
                raw_path = self.fix_filenames(path_input.value)

                if not raw_path:
                    print("❌ Error: Path cannot be empty.")
                    return

                # Validate the filepath before adding
                if not CleanData.validate_filepaths(raw_path):
                    print(f"❌ Error: Invalid file path format for '{raw_path}'.\n          Please ensure it follows the correct file specification.")
                    return

                filename = Path(raw_path)

                # DEFENSIVE CHECK: Prevent duplicate entries in the manifest
                if filename in target_filenames:
                    print(f"⚠️ Warning: {filename.name} is already in the list.")
                    return

                target_filenames.append(filename)
                path_input.value = "" # Clear the box for the next entry

                clear_output(wait=True)
                print(f"✅ {filetype} Manifest Updated:")
                for f in target_filenames:
                    print(f" - {f}")

        def on_finish_clicked(b):
            # LOCKING THE UI: Prevents changes after the user is finished
            path_input.disabled = True
            add_button.disabled = True
            finish_button.disabled = True
            with output_log:
                print(f"🚀 {filetype} Manifest finalized.")

        add_button.on_click(on_add_clicked)
        finish_button.on_click(on_finish_clicked)

        display(widgets.VBox([header, path_input, widgets.HBox([add_button, finish_button]), output_log]))

    def __import_files_jupyter_notebook(self, filetype):    
        """
        PRIVATE METHOD: Handles Local File Selection using standard input().
        Keeps the same robust validation but replaces complex UI with 
        a standard terminal-based workflow.
        """

        # Compute the PrivateClass parameters
        calling_function = inspect.stack()[1].function
        method_name = "_CleanData__import_files_jupyter_notebook"
        class_name = CleanData

        # 1. GATEKEEPING (Security intact)
        PrivateClass.check_valid_method_access(calling_function, method_name, class_name)

        # 2. ROUTING (Maintain your existing logic)
        filetype, target_filenames = self.__validate_filetype(filetype, self.__input_filenames, self.__output_filenames)

        print(f"\n--- Select {filetype} Files ---")
        print("Type your file paths one by one. Type 'done' when finished.")

        # 3. OLD SCHOOL LOOP
        while True:
            user_input = input(f"Enter {filetype} path: ").strip()
            
            if user_input.lower() == "done":
                print("🚀 Manifest Locked.")
                break
                
            # Standardize the path
            raw_path = self.fix_filenames(user_input)
            if not raw_path:
                print("❌ Error: Path cannot be empty.")
                continue

            # VALIDATION
            if not CleanData.validate_filepaths(raw_path):
                print(f"❌ Error: Invalid file path format for '{raw_path}'.")
                continue

            filename = Path(raw_path)
            if filename not in target_filenames:
                target_filenames.append(filename)
                print(f"✅ Added: {raw_path}")
            else:
                print("⚠️ Path already in manifest.")

    @staticmethod
    def __validate_filetype(filetype, input_filenames, output_filenames):
        """
        THE GATEKEEPER: Validates and routes data categories.

        This private static method ensures that only authorized data categories
        ("Input" or "Output") can proceed through the pipeline.
        """

        # Compute the PrivateClass parameters
        calling_function = inspect.stack()[1].function
        method_name = "_CleanData__validate_filetype"
        class_name = CleanData
                
        # Check for valid method access
        PrivateClass.check_valid_method_access(calling_function, method_name, class_name)
        
        if filetype.lower() == "input":
            if filetype != "Input":
                filetype = "Input"
            return filetype, input_filenames
        elif filetype.lower() == "output":
            if filetype != "Output":
                filetype = "Output"
            return filetype, output_filenames
        else:
            # SHIELDING: Halt execution if an invalid category is provided
            raise InvalidFileType(f'"{filetype}" is not a valid file type. (Must be "Input" or "Output")')

    @staticmethod
    def validate_filepaths(path_list):
        """
        PATH INTEGRITY ENGINE:
        Ensures all provided paths conform to operating system standards
        and internal environment specifications.

        This method handles 'Nested Complexity'—it can take a single path,
        a list of paths, or even a list of lists, and flattens them into
        a standard format for regex validation.
        """
        # --- 1. RECURSIVE FLATTENING ---
        # We ensure the input is always treated as a list, regardless of
        # whether the user provided a single string or a complex nested structure.
        flat_paths_as_strings = []

        if not isinstance(path_list, list):
            # POLYMORPHIC WRAPPING: Force single inputs into a list format
            path_list = [path_list]

        for item in path_list:
            if isinstance(item, list):
                # NESTED LIST HANDLING: Unpack sub-lists to ensure a flat manifest
                for sub_item in item:
                    if isinstance(sub_item, (str, Path)):
                        flat_paths_as_strings.append(str(sub_item))
            elif isinstance(item, (str, Path)):
                # STANDARD INPUT: Direct conversion of Path objects or strings
                flat_paths_as_strings.append(str(item))

        # --- 2. REGEX VALIDATION (The Pattern Matcher) ---
        # This complex Regex verifies:
        # A) The path starts with a valid Cloud or Local prefix
        # B) The directory names contain no illegal characters (e.g., < > : " | ?)
        # C) The string ends with a valid file extension
        if using_google_colab:
            pattern = re.compile(
                r'(?:/content/drive/MyDrive/|G:\\My Drive\\)' # Prefix check
                r'(?:[^<>:"/\\|?*\r\n]+[\\/])*'               # Folder structure
                r'[^<>:"/\\|?*\r\n]+\.'                       # Filename
                r'[^<>:"/\\|?*\r\n]+'                         # Extension
            )
        else:
            pattern = re.compile(
                r'^(?:[a-zA-Z]:\\|\\\\[^\\\/:*?"<>|\r\n]+\\[^\\\/:*?"<>|\r\n]+\\)' # Prefix check
                r'(?:[^\\\/:*?"<>|\r\n]+\\)*'                                      # Folder structure
                r'[^\\\/:*?"<>|\r\n]+\.[^\\\/:*?"<>|\r\n]+$'                       # Filename and Extension
            )

        # Returns a list of booleans (True/False) to the calling method
        if len(flat_paths_as_strings) == 1:
            return bool(pattern.search(flat_paths_as_strings[0]))
        else:
            return [bool(pattern.search(f)) for f in flat_paths_as_strings]

    @staticmethod
    def fix_filenames(path_list):
        """
        DATA NORMALIZATION & INPUT VALIDATION:
        Ensures internal logic remains case-insensitive and resilient to user typos.

        This method acts as a 'Sanity Check' for user-provided strings. By
        standardizing variations (e.g., 'input', 'INPUT') into a single
        canonical form ('Input'), we prevent downstream logic branches from
        failing due to casing mismatches.
        """

        # Check to see if the path_list is a string. (Convert it to a list)
        path_list_is_string = isinstance(path_list, str)
        if path_list_is_string:
            path_list = [path_list]

        # Convert Windows file path to the proper Google Drive Syntax
        if using_google_colab:
            fixed_filenames = [p.strip() \
                                .replace("G:\\My Drive\\", "/content/drive/MyDrive/") \
                                .replace('"', "") \
                                .replace("\\", "/") for p in path_list]
        else:
            fixed_filenames = [p.strip() \
                                .replace('"', "") \
                                .replace("/", "\\") for p in path_list]

        # Return the transformed filename
        if path_list_is_string:
            return fixed_filenames[0]
        else:
            return fixed_filenames

    def extract_filenames(self, convert_to_string=True, keep_as_list=False):
        """
        Returns a clean list of absolute file paths.
        Uses .resolve() to ensure paths are standardized across the system.
        """
        if convert_to_string:
            input_filenames = [str(f.resolve()) for f in self.__input_filenames]
            output_filenames = [str(f.resolve()) for f in self.__output_filenames]
        else:
            input_filenames = [f for f in self.__input_filenames]
            output_filenames = [f for f in self.__output_filenames]

        if len(input_filenames) == 1 and not keep_as_list:
            input_filenames = input_filenames[0]
        if len(output_filenames) == 1 and not keep_as_list:
            output_filenames = output_filenames[0]
        return input_filenames, output_filenames

    def remove_filenames(self, filetype, files_to_remove=None):
        filetype, target_filenames = self.__validate_filetype(filetype, self.__input_filenames, self.__output_filenames)

        original_target_filenames_str = [str(p) for p in target_filenames]
        print(f"Current {filetype} files: {original_target_filenames_str}")

        to_remove_paths_objects = [] # Actual Path objects to be removed
        display_remove_list = []     # For printing what we are attempting to remove

        if not files_to_remove:
            to_remove_paths_objects = list(target_filenames) # Mark all current paths for removal
            display_remove_list = "All files"
        elif isinstance(files_to_remove, int):
            if 0 <= abs(files_to_remove) < len(target_filenames)+int(files_to_remove < 0):
                # Remove by single index
                to_remove_paths_objects = [target_filenames[files_to_remove]]
                display_remove_list = [str(target_filenames[files_to_remove])]
            else:
                print(f"⚠️ Warning: Index {files_to_remove} is out of bounds for {filetype} files. No files removed.")
                return # Exit early if invalid index
        elif isinstance(files_to_remove, str):
            # Remove by single filename string
            fixed_path_str = CleanData.fix_filenames(files_to_remove)
            # Find the actual Path object in target_filenames that matches the fixed_path_str
            for p_obj in target_filenames:
                if str(p_obj) == fixed_path_str:
                    to_remove_paths_objects.append(p_obj)
                    break # Assuming unique paths, stop after first match
            if not to_remove_paths_objects:
                print(f"⚠️ Warning: File '{files_to_remove}' not found in {filetype} list. No files removed.")
                return # Exit early if file not found
            display_remove_list = [files_to_remove]
        elif isinstance(files_to_remove, list):
            # Check if list elements are strings or integers (assuming homogeneous list)
            if all(isinstance(item, str) for item in files_to_remove):
                # List of strings (filenames)
                fixed_paths_strs = CleanData.fix_filenames(files_to_remove)
                # Filter target_filenames to find actual Path objects that match the fixed_paths_strs
                to_remove_paths_objects = [p_obj for p_obj in target_filenames if str(p_obj) in fixed_paths_strs]
                if not to_remove_paths_objects:
                    print(f"⚠️ Warning: None of the specified files found in {filetype} list. No files removed.")
                    return
                display_remove_list = files_to_remove
            elif all(isinstance(item, int) for item in files_to_remove):
                # List of integers (indices)
                valid_indices_to_display = []
                for idx in files_to_remove:
                    if 0 <= abs(idx) < len(target_filenames)+int(idx < 0):
                        to_remove_paths_objects.append(target_filenames[idx])
                        valid_indices_to_display.append(str(target_filenames[idx])) # Store file path for display
                    else:
                        print(f"⚠️ Warning: Index {idx} is out of bounds for {filetype} files and will be skipped.")                        
                if not to_remove_paths_objects: # All indices were invalid or list was empty
                    print(f"⚠️ Warning: No valid indices provided for removal. No files removed.")
                    return
                display_remove_list = valid_indices_to_display
            else:
                print(f"❌ Error: List elements must be all strings or all integers. Mixed types are not supported.")
                return # Exit early for invalid list types
        else:
            raise TypeError(f"Unsupported type for files_to_remove: {type(files_to_remove)}. Must be int, str, or list.")

        print(f"Attempting to remove: {display_remove_list}")

        # Convert to_remove_paths_objects to a set of strings for efficient lookup during filtering
        to_remove_paths_str_set = {str(p) for p in to_remove_paths_objects}

        # Filter out the files that should be removed. Modify the list in place.
        target_filenames[:] = [p for p in target_filenames if str(p) not in to_remove_paths_str_set]

        print(f"After removal, {filetype} files: {[str(p) for p in target_filenames]}")

    def print_filenames(self):
        """
        Utility method to display the current manifest to the console.
        """
        input_filenames, output_filenames = self.extract_filenames(keep_as_list=True)

        print("Input Files:")
        if not input_filenames:
            print("- None")
        else:
            for path in input_filenames:
                print(f"- {path}")

        print("\nOutput Files:")
        if not output_filenames:
            print("- None")
        else:
            for path in output_filenames:
                print(f"- {path}")
        
    def process_files(self, cleaning_fun=None, **kwargs):
        """
        THE STRATEGY PATTERN: This allows the user to 'inject' custom cleaning
        logic into the class without modifying the class itself.
        """
        if not cleaning_fun:
            print("No cleaning function provided.")
        elif not self.__input_filenames and not self.__output_filenames:
            print("No files have been imported.")
        else:
            # Executes the injected function and stores the resulting DataFrame
            self.data_frame = cleaning_fun(self, **kwargs)
            print("Cleaning logic executed successfully.")
        return self.data_frame

# --- CUSTOM EXCEPTION ---
class InvalidFileType(Exception):
    """Raised when an unsupported file category is requested."""
    def __init__(self, message):
        super().__init__(message)

class PrivateClass:

    @staticmethod
    def check_valid_property_assignment(calling_function, access_name, public_property_names, class_name):
        case1 = any([calling_function in v[0] for v in vars(class_name).items()]) and access_name not in public_property_names
        case2 = access_name in public_property_names
        return case1 or case2
    
    @staticmethod
    def check_valid_method_access(calling_function, method_name, class_name):
        if not any([calling_function in v[0] for v in vars(class_name).items()]):          
            raise AttributeError(f"Access to private method '{method_name}' is forbidden.")