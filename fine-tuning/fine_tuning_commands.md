# checking my examples
export OPENAI_API_KEY=""
openai tools fine_tunes.prepare_data -f fine-tuning/fine_tuning_examples.jsonl

It thought that I was doing classification, but I am not. It also recommended to make more examples. We shall see how it goes.

# Training command
openai api fine_tunes.create -t fine-tuning/fine_tuning_examples_prepared_train.jsonl -v fine-tuning/fine_tuning_examples_prepared_valid.jsonl -m curie

# Results
Went well, but it could be better so I am going to add more training examples.
