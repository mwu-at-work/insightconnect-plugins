from komand_string import connection, actions, triggers


def handler(event, context):
    print(f'action name is {event.get("action_name")}')
    print(f'action input is {event.get("input")}')
    obj = "actions" + "." + event.get("action_name") + "()"
    action_obj = eval(obj)
    result = action_obj.run(event.get('input'))
    return result
