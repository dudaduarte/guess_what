from guess_what import io

def test_answer():
    assert io.enumerated_list_str(['Primeiro', 'Segundo', 'Terceiro']) == '1 - Primeiro\n2 - Segundo\n3 - Terceiro'
