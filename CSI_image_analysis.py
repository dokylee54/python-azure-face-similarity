import cognitive_face as CF
import glob
import os

import parameters


'''
server for hosting a profile image: 
    
    github

output format:

    /Users/dokylee/Desktop/dokylee/girlsinICT/dev/face_images/rocky3.jpg
        - Similarity
        {'isIdentical': True, 'confidence': 0.70765} 

    /Users/dokylee/Desktop/dokylee/girlsinICT/dev/face_images/rocky2.jpg
        - Similarity
        {'isIdentical': True, 'confidence': 0.64596} 

    /Users/dokylee/Desktop/dokylee/girlsinICT/dev/face_images/ggobuk.jpg
    ERROR in  /Users/dokylee/Desktop/dokylee/girlsinICT/dev/face_images/ggobuk.jpg : face is not detected...

    /Users/dokylee/Desktop/dokylee/girlsinICT/dev/face_images/thor.png
        - Similarity
        {'isIdentical': False, 'confidence': 0.11609} 



        ** Percentage of matcing = 0.5 %

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
    images = glob.glob(parameters.images_to_compare_path + '*.*')
    cnt = 0

    for img in images:

        print(img)

        # create a pair of images to compare
        img_compare = [ profile_imgURL, img ]

        # detect a face in each of the images
        faces = [CF.face.detect(img_url) for img_url in img_compare]

        # if face is not detected in the 'img' -> continue
        if not faces[1]:
            print('ERROR in ',img, ': face is not detected...\n')
            continue

        # compare two faces
        each_similarity = CF.face.verify(faces[0][0]['faceId'], faces[1][0]['faceId'])

        # if it is a same person -> cnt + 1
        if(each_similarity['isIdentical'] == True) : 
            cnt += 1

        # print the result
        print("\t- Similarity\n", "\t" + str(each_similarity), '\n')

    # print similarity
    similarity = cnt / len(images)
    print("\n\n\t** Percentage of matching =", str(similarity) + " %" )