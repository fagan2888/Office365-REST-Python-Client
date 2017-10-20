from tests.sharepoint_case import SPTestCase


class TestListItem(SPTestCase):
    target_list = None

    def setUpClass(self):
        super().setUpClass()
        self.target_list = self.context.web.lists.get_by_id("f15b5b99-f7b6-49d2-be85-81a51fdf52eb")  # Tasks

    def test_create_list_item(self):
        item_properties = {'Title': 'New Task', '__metadata': {'type': 'SP.Data.TasksListItem'}}
        item = self.target_list.add_item(item_properties)
        self.context.execute_query()
        print('List item \'{0}\' has been created.'.format(item.properties["Title"]))
