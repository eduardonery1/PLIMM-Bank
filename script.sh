

//Catador
curl -X POST https://api-hml.paysmart.com.br/paySmart/ps-processadora/v1/accounts/cta-3222e521-15fc-4952-88b4-6aa1cb47b7ee/virtualcards \
-H  "IdempotencyKey: 8e55675e-f284-4552-8deb-0fdfa0b204d9" \
-H  "API-Key: 5625cd6f9191c4a3f31f15d5a661ded3fa2688c5" \
-H  "accept: application/json" -H  "Content-Type: application/json" -d '
{
        "birthDate": "21/03/1983",
        "constraints": {
            "currency_code": 986,
            "max_amount": "*",
            "usage_limit": "*",
            "expiration_timestamp": "*"
        }
}'

//Super Mercado
curl -X POST https://api-hml.paysmart.com.br/paySmart/ps-processadora/v1/accounts/cta-ea369b21-ab22-444c-9d38-13df50015b1e/virtualcards \
-H  "IdempotencyKey: 8e55675e-f284-4552-8deb-0fdfa0b204b4" \
-H  "API-Key: 5625cd6f9191c4a3f31f15d5a661ded3fa2688c5" \
-H  "accept: application/json" -H  "Content-Type: application/json" -d '
{
        "birthDate": "21/03/1983",
        "constraints": {
            "currency_code": 986,
            "max_amount": "*",
            "usage_limit": "*",
            "expiration_timestamp": "*"
        }
}'
//Pessoa Física

curl -X POST https://api-hml.paysmart.com.br/paySmart/ps-processadora/v1/accounts \
-H  "IdempotencyKey: c354bf94-3d7d-11eb-9d51-0242ac130002" \
-H  "API-Key: 5625cd6f9191c4a3f31f15d5a661ded3fa2688c5" \
-H  "accept: application/json" -H  "Content-Type: application/json" -d '
{
  "psProductCode": "081002",
  "accountOwner": {
    "fullName": "Catador",
    "identityDocumentNumber": "03873903802",
    "contactInformation": { "personalPhoneNumber1": "+5551912345678",  "email": "fulano.silva@gmail.com" }
  },
  "billingAddress": {
    "addressLine1": "R. Manoelito de Ornellas",
    "addressLine2": "55",
    "city": "Porto Alegre",
    "state": "RS",
    "neighborhood": "Praia de Belas",
    "zipcode": "990000"
  },
  "cardDeliveryAddress": {
    "addressLine1": "R. Manoelito de Ornellas",
    "addressLine2": "55",
    "city": "Porto Alegre",
    "state": "RS",
    "neighborhood": "Praia de Belas",
    "zipcode": "990000"
  }
}'



curl -X POST https://api-hml.paysmart.com.br/paySmart/ps-processadora/v1/accounts \
-H  "IdempotencyKey: 4dd71cca-d89a-4cc0-8e16-f524da933432" \
-H  "API-Key: 55625cd6f9191c4a3f31f15d5a661ded3fa2688c5" \
-H  "accept: application/json" -H  "Content-Type: application/json" -d '
{
  "psProductCode": "001002",
  "accountOwner": {
    "fullName": "Super Mercado",
    "identityDocumentNumber": "03873703805",
    "contactInformation": { "personalPhoneNumber1": "+5551912345678",  "email": "fsuper.silva@gmail.com" }
  },
  "billingAddress": {
    "addressLine1": "R. Manoelito de Ornellas",
    "addressLine2": "55",
    "city": "Porto Alegre",
    "state": "RS",
    "neighborhood": "Praia de Belas",
    "zipcode": "990000"
  },
  "cardDeliveryAddress": {
    "addressLine1": "R. Manoelito de Ornellas",
    "addressLine2": "55",
    "city": "Porto Alegre",
    "state": "RS",
    "neighborhood": "Praia de Belas",
    "zipcode": "990000"
  }
}'

curl -X POST https://api-hml.paysmart.com.br/paySmart/ps-processadora/v1/accounts \
-H  "IdempotencyKey: 4dd71cca-d89a-4cc0-8e16-f524da933452" \
-H  "API-Key: 55625cd6f9191c4a3f31f15d5a661ded3fa2688c5" \
-H  "accept: application/json" -H  "Content-Type: application/json" -d '
{
  "psProductCode": "001002",
  "accountOwner": {
    "fullName": "Catador Legal",
    "identityDocumentNumber": "03873703805",
    "contactInformation": { "personalPhoneNumber1": "+5551912345678",  "email": "catador.silva@gmail.com" }
  },
  "billingAddress": {
    "addressLine1": "R. Manoelito de Ornellas",
    "addressLine2": "55",
    "city": "Porto Alegre",
    "state": "RS",
    "neighborhood": "Praia de Belas",
    "zipcode": "990000"
  },
  "cardDeliveryAddress": {
    "addressLine1": "R. Manoelito de Ornellas",
    "addressLine2": "55",
    "city": "Porto Alegre",
    "state": "RS",
    "neighborhood": "Praia de Belas",
    "zipcode": "990000"
  }
}'


