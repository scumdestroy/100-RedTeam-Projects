import lief
import pefile
import sys

exe_path = sys.argv[1]

fd = open(exe_path, 'rb')
pe_data = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ)

# Parse the executable, my boy
# If file is larger than 3MB, prevent parsing the directories
if os.path.getsize(exe_path) > 3145728:
    pe = pefile.PE(data=pe_data, fast_load=True)
else:
    pe = pefile.PE(data=pe_data)
    
# Get the entry point
entry_point = pe.OPTIONAL_HEADER.AddressOfEntryPoint
entry_point += pe.OPTIONAL_HEADER.ImageBase

# Get the sections
sections = pe.sections
imports = pe.DIRECTORY_ENTRY_IMPORT
exports = pe.DIRECTORY_ENTRY_EXPORT
resources = pe.DIRECTORY_ENTRY_RESOURCE
relocations = pe.DIRECTORY_ENTRY_BASERELOC
tls = pe.DIRECTORY_ENTRY_TLS
debug = pe.DIRECTORY_ENTRY_DEBUG
load_config = pe.DIRECTORY_ENTRY_LOAD_CONFIG
bound_import = pe.DIRECTORY_ENTRY_BOUND_IMPORT
delay_import = pe.DIRECTORY_ENTRY_DELAY_IMPORT
exception = pe.DIRECTORY_ENTRY_EXCEPTION
security = pe.DIRECTORY_ENTRY_SECURITY
architecture = pe.FILE_HEADER.Machine
timestamp = pe.FILE_HEADER.TimeDateStamp
size = pe.OPTIONAL_HEADER.SizeOfImage
checksum = pe.OPTIONAL_HEADER.CheckSum
subsystem = pe.OPTIONAL_HEADER.Subsystem
dll_characteristics = pe.OPTIONAL_HEADER.DllCharacteristics
magic = pe.OPTIONAL_HEADER.Magic
linker_version = pe.OPTIONAL_HEADER.MajorLinkerVersion

# print the entry_point, sections, functions, strings , etc...  and organize into a neat chart and save to a markdown file
print("Entry_Point: " + pe.OPTIONAL_HEADER.AddressOfEntryPoint)
print("Sections: " + pe.sections)   
print("Headers\n--------------\n" + pe.print_info()

# Print the imports
print("Printing Imports...\n")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print(entry.dll)
    for imp in entry.imports:
        print('\t', hex(imp.address), imp.name)
        
# Print the exports
print("Printing Exports...\n")
for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
    print(hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal)
    
# Print the resources
print("Printing Resources...\n")



# Print the relocations
print("Printing Relocations...\n")
for base_reloc in pe.DIRECTORY_ENTRY_BASERELOC:
    print(hex(base_reloc.virtual_address))
    for reloc in base_reloc.entries:
        print('\t', hex(reloc.address), reloc.type)
        
# Print the TLS
print("Printing TLS...\n")
for tls in pe.DIRECTORY_ENTRY_TLS:
    print(hex(tls.struct.AddressOfCallBacks))
    for callback in tls.callbacks:
        print('\t', hex(callback))
        
# Print the debug
print("Printing Debug...\n")
for dbg in pe.DIRECTORY_ENTRY_DEBUG:
    print(hex(dbg.struct.AddressOfRawData), dbg.struct.PointerToRawData)
    
# Print the load config
print("Printing Load Config...\n")
print(pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.Size)
print(pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.TimeDateStamp)
print(pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.MajorVersion)
print(pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.MinorVersion)
print(pe.DIRECTORY_ENTRY_LOAD_CONFIG.struct.GlobalFlagsClear)

# Print the bound import
print("Printing Bound Import...\n")
for bound_import in pe.DIRECTORY_ENTRY_BOUND_IMPORT:
    print(bound_import.struct.TimeDateStamp)
    print(bound_import.struct.OffsetModuleName)
    for entry in bound_import.entries:
        print('\t', hex(entry.struct.TimeDateStamp), entry.struct.OffsetModuleName)
        
# Print the delay import
print("Printing Delay Import...\n")
for entry in pe.DIRECTORY_ENTRY_DELAY_IMPORT:
    print(entry.dll)
    for imp in entry.imports:
        print('\t', hex(imp.struct.AddressOfData), imp.struct.Name)
        
# Print the exception
print("Printing Exception...\n")
for entry in pe.DIRECTORY_ENTRY_EXCEPTION:
    print(hex(entry.struct.StartingAddressOfRawData), entry.struct.EndingAddressOfRawData)
    print(hex(entry.struct.AddressOfHandler), entry.struct.AddressOfHandler)
    
# Print the security
print("Printing Security...\n")
print(hex(pe.DIRECTORY_ENTRY_SECURITY.struct.VirtualAddress))
print(pe.DIRECTORY_ENTRY_SECURITY.struct.Size)

# Print the architecture
print("Printing Architecture...\n")
print(pe.FILE_HEADER.Machine)

# Print the timestamp
print("Printing Timestamp...\n")
print(pe.FILE_HEADER.TimeDateStamp)

print("Size: " + pe.OPTIONAL_HEADER.SizeOfImage)
print("Checksum: " + pe.OPTIONAL_HEADER.CheckSum)
print("Subsystem: " + pe.OPTIONAL_HEADER.Subsystem)
print("DLL_Characteristics: " + pe.OPTIONAL_HEADER.DllCharacteristics)
print("Magic: " + pe.OPTIONAL_HEADER.Magic)
print("Linker_Version: " + pe.OPTIONAL_HEADER.MajorLinkerVersion)

