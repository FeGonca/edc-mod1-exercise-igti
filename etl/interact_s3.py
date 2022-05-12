
# import boto3
# import os

# def upload_s3():
#     # Cliente para interagir com o AWS S3
#     s3_client = boto3.client('s3')

#     # Lista os arquivos para subir no s3
#     dlpath = '../data/rais'
#     lista_arquivo = os.listdir(dlpath)

#     for i in range(len(lista_arquivo)):
#         filename = dlpath + '/' + lista_arquivo[i]
#         file = lista_arquivo[i]
#         object_name  = 'rais/' + lista_arquivo[i]
#         bucket = 'igti-felipe-rais-default-landing-zone-539475468352'
#         s3_client.upload_file(filename, bucket, object_name)

# if __name__ == "__main__":
#     upload_s3()        