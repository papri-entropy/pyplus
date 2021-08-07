def test_find_prompt(netmiko_conn):
    assert "arista1" in netmiko_conn.find_prompt()

def test_show_version(netmiko_conn):
    output = netmiko_conn.send_command("show version")
    assert "4.20.10M" in output
