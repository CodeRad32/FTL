# Custom_token.pl

# Tokens starting with '!'
my @tokens_bang = qw(
    ! @ !# !$ !% !^ !& !* !( !) !! !@
);

# Tokens starting with '@'
my @tokens_at = qw(
    @) @! @@ @# @$ @% @^ @& @* @(
);

# Tokens starting with '#'
my @tokens_hash = qw(
    #) #! #@ ## #$ #% #^ #& #* #(
);

# Tokens starting with '$'
my @tokens_dollar = qw(
    $) $! $@ $# $$ $% $^ $& $* $(
);

# Tokens starting with '%'
my @tokens_percent = qw(
    %) %! %@ %# %$ %% %^ %& %* %(
);

# Tokens starting with '^'
my @tokens_caret = qw(
    ^) ^! ^@ ^# ^$ ^% ^^ ^& ^* ^(
);

# Tokens starting with '&'
my @tokens_amp = qw(
    &) &! &@ & # & $ & % & ^ & & & * &( 
);

# Tokens starting with '*'
my @tokens_star = qw(
    *) *! *@ *# *$ *% *^ *& ** *(
);

# Tokens starting with '('
my @tokens_paren = qw(
    () (! (@ (# ($ (% (^ (& (* (()
);

# Tokens starting with '!))'
my @tokens_bang_close = qw(
    !))
);

# Combine all tokens into a single array
my @all_tokens = (
    @tokens_bang, @tokens_at, @tokens_hash, @tokens_dollar,
    @tokens_percent, @tokens_caret, @tokens_amp, @tokens_star,
    @tokens_paren, @tokens_bang_close
);

# Print the tokens for verification
foreach my $token (@all_tokens) {
    print "$token\n";
}
