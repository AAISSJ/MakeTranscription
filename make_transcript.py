import os 
from google.cloud import storage
from google.cloud import speech_v1p1beta1 as speech

# load audio file names

data_folder1 = '/home/dsail/sejeong/2023/Dementia/Data/MADReSS/sample'
data_folder2 = '/home/dsail/sejeong/2023/Dementia/Data/MADReSS/train'

file_list1 = os.listdir(data_folder1)
file_list2 = os.listdir(data_folder2)

file_list = file_list1 + file_list2

# make transcription and save text files

for file_name in file_list :
    uri = 'gs://dementiaspeech/'+file_name
    # Encoding: https://cloud.google.com/
    # speech-to-text/docs/reference/rest/v1beta1/RecognitionConfig
    encoding='MP3'
    sample_rate_hertz=44100
    # Language: https://cloud.google.com/
    # speech-to-text/docs/languages
    language_code='es-US' 	#en-EN #es-ES
    
    f = open('/PATH/to/dir/transcript/es/'+file_name[:-4]+'_es.txt', 'w')

    client = speech.SpeechClient.from_service_account_json('/PATH/to/json_dir/YOUR_SERVICE_ACCOUNT_JSON')
    operation = client.long_running_recognize( 
            audio=speech.types.RecognitionAudio(uri=uri),
            config=speech.types.RecognitionConfig(
                    encoding=encoding,
                    sample_rate_hertz=sample_rate_hertz,
                    language_code=language_code,
                    use_enhanced=True,
                    model='latest_long',
                    profanity_filter=False,
                    enable_automatic_punctuation=True,
                    enable_word_confidence=True))
    op_result = operation.result()
    for result in op_result.results:
        for alternative in result.alternatives:
            #print('=' * 20)
            #print(alternative.transcript)
            #print(alternative.confidence)
            f.writelines(alternative.transcript+'\t'+str(alternative.confidence)+'\n')

    f.close()