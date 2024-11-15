# CCFToolkit

CCFToolkit is a Python module designed for reading and generating Paintman CCF (Color Chart File) files, commonly used in color chart management for animation production. It supports both 8-bit and 16-bit(read-only) RGB color depths.

## Installation

To install CCFToolkit, use `pip`:

```bash
pip install CCFToolkit
```

## Usage

### Importing the Module
```python
from CCFToolkit import CCFGenerator, CCFReader, RGB8, RGB16
```

### Creating a CCF File
You can generate a CCF file using `CCFGenerator`:

```python
color_data = [
    ((255, 0, 0), "Red"),
    ((0, 255, 0), "Green"),
    ((0, 0, 255), "Blue峠"),
    ((0, 0, 0), "黑色辻"),  # Example with Chinese characters
    ((255, 255, 255), "White白色"),  # Example with Japanese characters
    ((128, 128, 128), "Gray灰色"),
    ((255, 255, 0), "Yellow"),
    ((0, 255, 255), "Cyanシアン"),  # Japanese characters
    ((255, 0, 255), "Magenta")
]

generator = CCFGenerator(color_data)
generator.create_ccf_file("output_file.ccf")
print("CCF file created successfully at 'output_file.ccf'")
```

### Reading a CCF File
You can read a CCF file using `CCFReader`:

```python
reader = CCFReader("output_file.ccf")

# Reading with 8-bit RGB
color_data_8bit = reader.read_ccf_file(RGB8)
print("8-bit RGB Color Data:")
for label, rgb in color_data_8bit:
    print(f"Label: {label}, RGB: {rgb}")

# Reading with 16-bit RGB
color_data_16bit = reader.read_ccf_file(RGB16)
print("\n16-bit RGB Color Data:")
for label, rgb in color_data_16bit:
    print(f"Label: {label}, RGB: {rgb}")
```

## Constants

- `RGB8`: Integer constant representing 8-bit RGB color depth.
- `RGB16`: Integer constant representing 16-bit RGB color depth.

## Exception Handling
- `CCFGenerator` raises a `ValueError` if any RGB value exceeds 255, ensuring the values are valid 8-bit RGB before encoding.

## Important Notes
- Current version of `CCFGenerator` does not support 16-bit RGB or RGBA encoding.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.

## Contact
For questions or support, feel free to pull a request or issue.

---

Enjoy using `CCFToolkit` for your color chart management in animation projects!
