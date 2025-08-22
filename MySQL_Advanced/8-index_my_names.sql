-- Create index on names, first letter of name
CREATE INDEX idx_name_first ON names(name(1));