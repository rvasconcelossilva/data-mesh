from pulumi.automation import create_or_select_stack, ConfigValue

class Stack():

    def __init__(self, stack_name, project_name, resources): 
        self._stack_name = stack_name
        self._project_name = project_name
        self._resources = resources

    def build(self):
        for resource in self._resources:
            self._stack = create_or_select_stack(
                stack_name=self._stack_name,
                project_name=self._project_name,
                program=resource.resource_program
            )

    def set_config(self, config: dict):
        for key, value in config.items():
            self._stack.set_config(key, ConfigValue(value=value))
                                                                                                       
    def up(self):
        self._stack.up(on_output=print)

    def destroy(self):
        self._stack.destroy(on_output=print)

    def preview(self):
        self._stack.preview(on_output=print)        

