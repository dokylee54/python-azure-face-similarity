import cognitive_face as CF
import glob
import os

import parameters


'''
temporary server for hosting a profile image:

    https://imgbb.com/

'''


if __name__ == "__main__":
    
    ###
    # profile image URL
    profile_imgURL = parameters.profile_imgURL
    ###

    key = parameters.subscription_key  # Replace with a valid Subscription Key here.
    CF.Key.set(key)

    base_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
    CF.BaseUrl.set(base_url)

    # only jpg file
    images = glob.glob(parameters.images_to_compare_path + '*.jpg')
    cnt = 0

    for img in images:

        print(img)

        # create a pair of images to compare
        img_compare = [ profile_imgURL, img ]

        # detect a face in each of the images
        faces = [CF.face.detect(img_url) for img_url in img_compare]

        # compare two faces
        each_similarity = CF.face.verify(faces[0][0]['faceId'], faces[1][0]['faceId'])

        # if it is a same person -> cnt + 1
        if(each_similarity['isIdentical'] == True) : 
            cnt += 1

        # print the result
        print("< Similarity >", each_similarity)

    # print similarity
    similarity = cnt / len(images)
    print("\n\n** Percentage of matcing =", str(similarity) + " %" )