-- Create index names for the first letter of name and score
CREATE INDEX idx_name_first_score ON names(name(1), score(1));