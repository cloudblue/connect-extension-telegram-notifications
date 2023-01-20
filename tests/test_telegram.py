from connect_telegram_ext.telegram import convert_unsupported_tags


def test_convert_unsupported_tags():
    input_string = "<div>Hello World!</div>"
    expected_output = "&lt;div&gt;Hello World!&lt;/div&gt;"
    assert convert_unsupported_tags(input_string) == expected_output

    input_string = "<b>Bold text</b>"
    expected_output = "<b>Bold text</b>"
    assert convert_unsupported_tags(input_string) == expected_output

    input_string = "<p>This is <i>italic</i> text</p>"
    expected_output = "&lt;p&gt;This is <i>italic</i> text&lt;/p&gt;"
    assert convert_unsupported_tags(input_string) == expected_output

    input_string = "<code>print('Hello World!')</code>"
    expected_output = "<code>print('Hello World!')</code>"
    assert convert_unsupported_tags(input_string) == expected_output

    input_string = "there is an email <noreply-telefonicacloud@connect.cloudblue.com>"
    expected_output = "there is an email &lt;noreply-telefonicacloud@connect.cloudblue.com&gt;"
    assert convert_unsupported_tags(input_string) == expected_output
