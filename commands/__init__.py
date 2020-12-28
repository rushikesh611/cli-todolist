import commands.todos
import commands.list

commands_dict = {
  # 'show': list.show_lists,
  # 'use': list.use_list,
  # 'create': list.create_list,
  'add': todos.add_item,
  'ls': todos.show_items,
  # 'edit': todos.edit_item,
  'del': todos.remove_item,
  'done': todos.done,
  'report':todos.report,
  # 'incomplete': todos.incomplete_item
}