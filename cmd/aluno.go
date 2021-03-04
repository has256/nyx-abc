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

type aluno struct {
	NomeCompleto string `json:"fullname"`
	Usuario      string `json:"username"`
}

var (
	info         bool
	email        bool
	nomeCompleto bool
	usuario      bool
	alunoCmd     = &cobra.Command{
		Use:   "aluno",
		Short: "Utilitários relacionados à discentes",
		Run: func(cmd *cobra.Command, args []string) {
			if len(args) == 0 {
				cmd.Help()
				os.Exit(-1)
			}
			res, _ := http.Get("https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=2&valor=" + args[0])
			body, _ := ioutil.ReadAll(res.Body)
			discente := aluno{}
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
	rootCmd.AddCommand(alunoCmd)
	alunoCmd.Flags().BoolVarP(
		&info, "info",
		"i", false, "retorna as informacoes de algum(a) aluno(a)",
	)
	alunoCmd.Flags().BoolVarP(
		&email, "e-mail",
		"e", false, "retorna o e-mail de algum(a) aluno(a)",
	)
	alunoCmd.Flags().BoolVarP(
		&usuario, "usuario",
		"u", false, "retorna o usuario de algum(a) aluno(a)",
	)
	alunoCmd.Flags().BoolVarP(
		&nomeCompleto, "nome-completo",
		"n", false, "retorna o nome completo de algum(a) aluno(a)",
	)
}
