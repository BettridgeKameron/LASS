import stylocorp
import stylomod
import json
import os

def main():
    # json_string = '{"text_to_analyze": "this is a sample text a user put in the input box"}'
    # input = json.loads(json_string)

    dir = os.path.join("alvin_work","prints","formal")
    sep = "_-_"
    input = stylocorp.Corpus(dir,sep)
    print(input.prints[0].author)
    # print(stylomod.num_errors(input["text_to_analyze"]))

if __name__ == "__main__":
    main()