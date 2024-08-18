import os
from src.TextSum.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from src.TextSum.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        documents = example_batch['document']
        summaries = example_batch['summary']

    # Ensure that documents and summaries are lists of strings
        if isinstance(documents, list):
            documents = [str(doc) for doc in documents]
        else:
            documents = [str(documents)]

        if isinstance(summaries, list):
            summaries = [str(sum) for sum in summaries]
        else:
            summaries = [str(summaries)]

    # Tokenize inputs
        input_encodings = self.tokenizer(documents, max_length=1024, truncation=True, padding='max_length', return_tensors='pt')

    # Tokenize targets
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(summaries, max_length=128, truncation=True, padding='max_length', return_tensors='pt')

        return {
        'input_ids': input_encodings['input_ids'],
        'attention_mask': input_encodings['attention_mask'],
        'labels': target_encodings['input_ids']
    }

    def convert(self):
        dataset_edin = load_from_disk(self.config.data_path)
        dataset_edin_pt = dataset_edin.map(self.convert_examples_to_features, batched = True)
        dataset_edin_pt.save_to_disk(os.path.join(self.config.root_dir,"edin_dataset"))