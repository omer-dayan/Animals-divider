blacklist_keys = ['refers', 'to', 'all', 'species', 'of', 'genus', 'Bos', '.']


def generate_reverse_dictionary_by_table(table, key_column_name, value_column_name):
    result = {}
    for row in table.rows:
        if key_column_name not in row:
            continue

        first_value_word = row[value_column_name].value.split()[0]
        keys_with_spaces = row[key_column_name].value
        all_keys = keys_with_spaces.split()
        for key in all_keys:
            if is_key_in_blacklist(key):
                continue
            if key not in result:
                result[key] = []

            value = first_value_word
            if len(all_keys) > 1:
                value = value + ' ' + generate_other_keys_statement(all_keys, key)
            result[key].append(value)
    return result


#
# Method to check if some words should not be a key of the dictionary
# Currently we do not accept words in bracket (X) and words in black list
#
def is_key_in_blacklist(key):
    return key[:1] == '(' or any(key in item for item in blacklist_keys)


#
# Generate user statement to say that the instance may be in other keys
# (The animal have more collateral adjective)
#
def generate_other_keys_statement(all_keys, current_key):
    result = '(also '
    for key in all_keys:
        if is_key_in_blacklist(key):
            continue
        if key != current_key:
            result = result + key + ', '
    return result[:-2] + ')'
