def generate_class_def(class_name: str, attrs:dict, superclass_name:str,superclass_args:list=[]):    
    
    constructor_args = []
    constructor_def = ""
    has_attributes = False

    class_template = f"class {class_name}"

    if superclass_name:        
        class_template += f"({superclass_name})"
    
    class_template += ":\n"

    for attr_name in attrs.keys():
        if attr_name != "subclasses":
            has_attributes = True
            constructor_args.append(attr_name)
            constructor_def += f"\n\t\tself.{attr_name} = {attr_name}"

    if class_name == "Product":
            constructor_def += "\n\t\tself.name=type(self).__name__"

    if has_attributes:
        constructor_template = f"\tdef __init__(self, {', '.join(constructor_args+superclass_args)}):"

        if len(superclass_args)>0:
            constructor_template +=f"\n\t\tsuper().__init__({', '.join(superclass_args)})"

        constructor_template +=constructor_def
    
    else:
        if len(superclass_args)>0:
            constructor_template = f"\tdef __init__(self, {', '.join(superclass_args)}):"
            constructor_template +=f"\n\t\tsuper().__init__({', '.join(superclass_args)})"
      
        else:    
            constructor_template = "\tpass"

    return class_template + constructor_template + "\n\n"
