import requests
import random
import time
import json

nc_token = f'CF_APP_1:{round(time.time())}:{random.random()}'  # 模拟JS的nc_token CF_APP_1:timesmap:随机数
print(nc_token)
cookies = {'aliyun_choice': 'intl', '_ga': 'GA1.2.26226098.1596179861', '_gid': 'GA1.2.149344.1596179861'}
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36'}
analyze_json = requests.get('https://cf.aliyun.com/nocaptcha/analyze.jsonp', cookies=cookies, headers=headers, data={
    'a': 'FFFF0N000000000087DE',
    't': nc_token,
    'n': '125#coscaad4cWB0tq+hihfNUDNDjION3ytfLw/bD8VfVmej8/RTTukat3JFKm3XMBT1mpC5Yq4Q+3gB4pFjcuqhnC4jEEefuymUUjQc3PtZctR06hEGUZkckh3QWJ+jqpqZ7DKj8c/6NCo+7w/A/Q9Oz4yoDR/veAq1DJXgv546aStKz9gYgS5YUXNBzIRdv4DfYvVOL98lo6OcGG8A4iF0ZBE7XIaqVKKcIPJRaGSoQ878UXBiaQP/98E0skUkORozc/MYws80GMwFL8bmqqIp5nx7OzMpvj+KUjcScLWkaHvHUo1CKJEccUHiccVJEjcSU9iG9XwJc7el68NHP02GYGFrmOmAX8mVdRyX2j5pYG2DivSbYTt+D7troPLAsYO04ak8/07+1aceT3EarxapmVLfOW/fXIg14Oc3Ok1khl48oVsPxLD0sm4Z64QaKHAInBVo1tozGp7zyBInuLTquaK/c2/qbxK0SuQeYRnSD1geyhDnMtRkoZNQRn+4qouFRtaCc8YIRthzMhTuUEddNKyIr+UKetYc+oN3/SZwb25tvc0M4vEc60oXBGJd/hlIxc92Pq00VAlbV4wngX5L1peu1UtX6zZMR0mIaNj6jAB8l2/pmKtBlE1kxpRp9COIvMFQjDPtiNX5dMoSOFjgYODOpl8+Ew6INAMZH/SQmvnAWGIVCTpnSKxzZLE4/jkgpKl3Tooflf23buDr7ceyuRzRpnoGqKwsPG0RBPEhzB4XuKMIdHQSSYbYyoUhTYJ0agTtcmGLsU38LvJ/YMGipiUAKN7KOZas7aNaVaOti7VxmIbASVc/+n8Xwwq7mlAMiW3W+ptvY9qU3RTXi8RSaUZnpHApVa27ro9xC95c',
    'p': {"key1": "code0", "ncSessionID": "5e701eba9dcf",
          "umidToken": "T2gA1ACwi4kb1Uq9AOCuQqQ5aVwbDknPPTx5kP3DU26a3SQow_jHemH_d2XNvMC0DoRxNZum1yGJMIoAWGQh6bLO"},
    'callback': 'jsonp_08250975757696266'
})
print(analyze_json.text)

get_token = requests.get('http://47.56.160.68:81/api.php?sckey=y', headers=headers,
                         data={
                             'ym': 'kankanku.com',
                             'token': nc_token,
                             'authenticate': '05XqrtZ0EaFgmmqIQes-s-CIxgyTJyWdrBXU4H5giPeFOr1c6QVUtwpfqSNPdBVUFBrilnsxIyJS16ikaxyRY26fGZVNivFS3HNnJkB90Nq0OcI121Iv3RaxdBI1tpDFcVQl2MgeU_1GcqlK5ny-hPXvV9YCkL1bPqRs5H9bJXy1Zd-HI7EAoVgbw4gRVQlki9uU-ee_f3rCs2t6tBkqaG5Y3ntMPHMct7RJEojbh7LO-vrWGLzM8RifLFobn2tPABO6yd917Aw-xATZ57C9PUvLWLGqjCl4oiQD8DwIse34UFpL304cryRmDeUPkfJf-aYTCGQ_PyJQIKDLqopcmzsJcF6Q2gaT_pOMGwFnolPFpiCn4eLRQxIJUtrv1VpvEHf7iBiyoHVQH9cD7sLKxRdy6JXDTNikcJqvY_WjysitDcEKucYmmP_1x9WqYvbbHU',
                             'sessionid': '018erCRR715SHbswgnjvNYnAERKqRDq6NDQPOvyk-E_Ax_pYPSnBe34OXefJR6dOkIFiRJRrODbFWU2wA-FVg4l6_ijMiHM99ATKr2LD2tbEEoswFpbuRk3JI-nSWcLf2TRP4bCqEYdr939bBv9Ha7o3bJPqGPJLWc30YNPzuu1khsj5QSVBKnLYmk6KFml6-y'
                         })
print(get_token.text)
get_data = requests.post('http://47.56.160.68:81/api.php', data={
    'ym': 'star-robot.com',
    'xq': 'y',
    'page': '1',
    'limit': '20',
    'token': 'b417b',  # token 是我手动去网页上抓取的
    'group': '1',
})
print(get_data.json())
