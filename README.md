# System Info Fetcher

A lightweight, zero-dependency command-line utility to quickly display hardware and software information about your system.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Cross-Platform**: Works on Windows, macOS, and Linux.
*   **Zero Dependencies**: Uses only standard Python libraries (`platform`, `os`).
*   **JSON Output**: Option to export data for use in other scripts.

## Usage

```bash
python run_fetcher.py [options]
```

### Options

*   `--json`, `-j`: Output data in JSON format instead of a human-readable table.

### Example Output

```text
========================================
SYSTEM INFORMATION
========================================
OS             : Windows
OS Release     : 10
OS Version     : 10.0.19045
Architecture   : AMD64
Hostname       : WORKSTATION-PC
Processor      : Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
Python Version : 3.9.7
CPU Cores      : 8
Total Memory   : Unknown (psutil not installed)
----------------------------------------
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
