import ast
import importlib.util

filename = "thanos.py"

# محاولة فتح الملف بترميزات مختلفة
encodings_to_try = ["utf-8", "latin1", "cp1256"]

for enc in encodings_to_try:
    try:
        with open(filename, "r", encoding=enc) as f:
            content = f.read()
        break
    except UnicodeDecodeError:
        continue
else:
    print("❌ فشل في قراءة الملف بأي ترميز معروف")
    exit(1)

# تحليل الـ AST
tree = ast.parse(content, filename)

imports = set()

for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for n in node.names:
            imports.add(n.name.split(".")[0])
    elif isinstance(node, ast.ImportFrom):
        if node.module:
            imports.add(node.module.split(".")[0])

print(f"📦 المكتبات المستعملة في {filename}:")

for imp in sorted(imports):
    if importlib.util.find_spec(imp) is None:
        print(f"❌ ناقص: {imp}")
    else:
        print(f"✅ موجود: {imp}")

# اقتراح أوامر pip لكل المكتبات الناقصة
missing = [imp for imp in imports if importlib.util.find_spec(imp) is None]
if missing:
    print("\n💡 أوامر التثبيت المقترحة:")
    print("pip install " + " ".join(missing))