def validar_email(email):
    if email.count('@') != 1:
        return False
    parte_usuario, dominio = email.split('@')
    if len(parte_usuario) < 1:
        return False
    if '.' not in dominio:
        return False
    parte_dominio, ext = dominio.rsplit('.', 1)
    if len(parte_dominio) < 1 or len(ext) < 2:
        return False
    return True
