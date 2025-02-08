import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    lst = []
    for i in person.email:
        aux = 0
        for j in person.email:
            if i == j:
                aux += 1
                if aux > 1 and i not in lst:
                    lst.append(i)
    df = pd.DataFrame(data = {"email":lst})
    return df