# competition/metrics.py
from sklearn.metrics import f1_score

def macro_f1(y_true, y_pred):
    """
    Compute macro F1-score.
    y_true: true labels
    y_pred: predicted labels (0 or 1, or argmax for multi-class)
    """
    # if y_pred is probabilities, convert to predicted class
    if y_pred.ndim > 1:  
        y_pred = y_pred.argmax(axis=1)
    return float(f1_score(y_true, y_pred, average='macro'))
