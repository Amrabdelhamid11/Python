def names (amr,ali,ahmed):
    if amr >ali and amr >ahmed :
        return amr 
    elif ali > amr and ali > ahmed :
        return ali
    else:
        return ahmed
print(names(20,90,80))