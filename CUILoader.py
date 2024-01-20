import json
import umls_api


class AtomCUILoader:
    def __init__(self):
        self.api_key = 'api-key'
        self.cui_list = ['C0007107', 'C0004238', 'C0009264', 'C0012634', 'C1640363', 'C0242656', 'C5847618', 'C0012652', 'C0011900', 'C0011906', 'C0011911', 'C0332145', 'C0009473', 'C0282281', 'C0013227', 'C0812168', 'C0221423', 'C0242134', 'C0237087',
                    'C0282504', 'C0679247', 'C0344339', 'C2350572', 'C0424595', 'C0521117', 'C0496703', 'C0496703', 'C0521839', 'C0277793', 'C0278069', 'C0027765', 'C0149654']
        self.data_list = []

    def response_api(self):
        for cui in self.cui_list:
            self.response = umls_api.API(api_key=self.api_key).get_cui(cui=cui)
            print(self.response)
            self.data_list.append(self.response)
        return self.data_list

    def write_data_to_json(self):
        with open('../UMLSLoader/json_data.json', 'w') as outfile:
            json.dump(self.data_list, outfile)

if __name__ == '__main__':
    atom_cui = AtomCUILoader()
    atom_cui.response_api()
    atom_cui.write_data_to_json()