import requests
import pytest

url_ddg = "https://api.duckduckgo.com"
resp = requests.get(url_ddg + "/?q=presidents%20of%20the%20united%20states&format=json&pretty=1")
rsp_data = resp.json()
    
@pytest.mark.parametrize("president_name", ['Washington',
                                            'Adams',
                                            'Jefferson',
                                            'Madison',
                                            'Monroe',
                                            'Adams',
                                            'Jackson',
                                            'Van Buren',
                                            'Harrison',
                                            'Tyler',
                                            'Polk',
                                            'Taylor',
                                            'Fillmore',
                                            'Pierce',
                                            'Buchanan',
                                            'Lincoln',
                                            'Johnson',
                                            'Grant',
                                            'Hayes',
                                            'Garfield',
                                            'Arthur',
                                            'Cleveland',
                                            'Harrison',
                                            'Cleveland',
                                            'McKinley',
                                            'Roosevelt',
                                            'Taft',
                                            'Wilson',
                                            'Harding',
                                            'Coolidge',
                                            'Hoover',
                                            'Roosevelt',
                                            'Truman',
                                            'Eisenhower',
                                            'Kennedy',
                                            'Johnson',
                                            'Nixon',
                                            'Ford',
                                            'Carter',
                                            'Reagan',
                                            'Bush',
                                            'Clinton',
                                            'Bush',
                                            'Obama',
                                            'Trump'])
def test_ddg_presidents(president_name):
    assert any(president_name in data['Text'] for data in rsp_data['RelatedTopics'])

