class NotImplementedException(Exception):
    
    def __init__(self, crud_component, crud_operation):
        super().__init__()
        self.crud_component = crud_component
        self.crud_operation = crud_operation
