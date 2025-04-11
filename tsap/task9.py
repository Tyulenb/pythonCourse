import re


def main(string):
    pattern = r"\.\s*do\s*set\s*@'([^']+)'\s*<\|\s*([^\s]+)\.\s*\.\s*end"
    matches = re.findall(pattern, string)
    
    return matches

print(main("<< .do set @'gelaed_31' <| qudiar. .end, .do set @'isve' <| rieses. .end, >>"))
print(main("<< .do set @'arer_232' <| raquti. .end, .do set @'qusobe' <|qureve_860. .end, .do set @'teisar' <| bied. .end, .do set @'arorge' <| disoan_157. .end, >>"))
