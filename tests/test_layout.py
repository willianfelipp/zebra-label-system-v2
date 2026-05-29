from app.layouts.layout_loader import LayoutLoader

layout = LayoutLoader.load()

print(layout["name"])
print(layout["width_mm"])
print(layout["height_mm"])
print(layout["fields"])