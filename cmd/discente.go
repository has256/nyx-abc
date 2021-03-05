package cmd

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"github.com/spf13/cobra"
)

type discente struct {
	NomeCompleto string `json:"fullname"`
	Usuario      string `json:"username"`
}

var (
	info         bool
	email        bool
	nomeCompleto bool
	usuario      bool
	discenteCmd  = &cobra.Command{
		Use:   "discente",
		Short: "Utilitários relacionados à discentes",
		Run: func(cmd *cobra.Command, args []string) {

			if len(args) == 0 {
				cmd.Help()
				os.Exit(-1)
			}

			res, _ := http.Get("https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=2&valor=" + args[0])
			body, _ := ioutil.ReadAll(res.Body)
			discente := discente{}
			jsonErr := json.Unmarshal(body, &discente)

			if jsonErr != nil {
				log.Fatal(jsonErr)
			}

			if info {
				fmt.Println(discente)
			} else if email {
				fmt.Println(discente.Usuario + "@aluno.ufabc.edu.br")
			} else if usuario {
				fmt.Println(discente.Usuario)
			} else if nomeCompleto {
				fmt.Println(discente.NomeCompleto)
			}

		},
	}
)

func init() {

	type MyFlag struct {
		refVerbose  *bool
		verboseFlag string
		shortFlag   string
		hasFlag     bool
		description string
	}

	var myFlags []MyFlag
	myFlags = []MyFlag{
		{&info, "info", "i", false, "retorna as informacoes de algum(a) discente"},
		{&email, "email", "e", false, "retorna o e-mail de algum(a) discente"},
		{&usuario, "usuario", "u", false, "retorna o usuario de algum(a) discente"},
		{&nomeCompleto, "nome-completo", "n", false, "retorna o nome completo de algum(a) discente"},
	}

	for _, flag := range myFlags {
		discenteCmd.Flags().BoolVarP(
			flag.refVerbose,
			flag.verboseFlag,
			flag.shortFlag,
			flag.hasFlag,
			flag.description,
		)
	}

	rootCmd.AddCommand(discenteCmd)
}
