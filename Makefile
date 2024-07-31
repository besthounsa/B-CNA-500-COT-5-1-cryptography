PYTHON = python3
SRC_DIR = src
MAIN_FILE = $(SRC_DIR)/mypgp.py
PYFILES = $(SRC_DIR)/aes.py $(SRC_DIR)/pgp.py $(SRC_DIR)/rsa.py $(SRC_DIR)/utils.py $(SRC_DIR)/xor.py
PYCACHE = $(SRC_DIR)/__pycache__
PYCFILES = $(PYCACHE)/*.pyc
TARGET = $(SRC_DIR)/mypgp

# Règle par défaut
all: $(TARGET)

# Compilation du fichier principal en exécutable dans le dossier src
$(TARGET): $(MAIN_FILE)
	cp $< $@
	chmod +x $@

# Nettoyage des fichiers générés
clean:
	rm -rf $(PYCFILES) $(TARGET)

# Nettoyage complet (y compris l'exécutable)
fclean: clean
	rm -f $(TARGET)

# Règle pour recréer l'exécutable après un nettoyage
re: fclean all
