import pefile
import sys

origdll = sys.argv[1]

dll = pefile.PE(f'{origdll}_orig.dll')

print("EXPORTS")
for export in dll.DIRECTORY_ENTRY_EXPORT.symbols:
    if export.name:
        print(f'{export.name.decode()}={origdll}_orig.{export.name.decode()} @{export.ordinal}')
