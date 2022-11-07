compra = float (input('Valor gasto em compras R$ '))
print ('''
FORMA DE PAGAMENTO
[1] Á VISTA DÉBITO
[2] Á VISTA CRÉDITO
[3] 2X NO CRÉDITO
[4] 3X OU MAIS NO CRÉDITO
''')
opcao = int (input ('Qual forma de pagamento deseja: '))
vista_debito = compra - ((compra * 10)/100)
vista_credito = compra - ((compra * 5)/100)
credito_2 = compra / 2
credito_3 = compra + ((compra *20)/100)
if opcao == 1:
  print (f'Valor de compra R$ {compra:.2f} á vista de Débito R$ {vista_debito:.2f} com 10% de desconto')
elif opcao == 2:
  print (f'Valor da compra R$ {compra:.2f} á vista no Crédito R$ {vista_credito:.2f} com 5% de desconto')
elif opcao == 3:
  print (f'Valor da compra R$ {compra:.2f} em 2x de {credito_2:.2f} ')
elif opcao == 4:
  parcelas = int (input ('Em quantas parcelas: '))
  print (f'Valor da compra R$ {compra:.2f} ficará {parcelas}X de R$ {credito_3/parcelas:.2f} Total R$ {credito_3:.2f} ')