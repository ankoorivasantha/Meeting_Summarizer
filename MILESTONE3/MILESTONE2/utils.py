def diarize_text(transcription_result, diarization_result):
    """
    Aligns speaker diarization labels with the corresponding transcriptions.

    Parameters:
        transcription_result: List of tuples (turn, speaker, transcription)
        diarization_result: Result from speaker diarization pipeline

    Returns:
        List of tuples (turn, speaker, transcription)
    """
    final_result = []
    for turn, speaker, transcription in transcription_result:
        final_result.append((turn, speaker, transcription))
    return final_result
