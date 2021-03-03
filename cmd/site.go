package cmd

import (
	"log"
	"os"
	"os/exec"

	"github.com/spf13/cobra"
)

func openBrowser(url string) {
	var err error
	exec.Command("xdg-open", url).Start()
	if err != nil {
		log.Fatal(err)
	}
}

var (
	tidia   bool
	prograd bool
	gradmat bool
	bcc     bool
	sigaa   bool
	moodle  bool
	neuro   bool
	ufabc   bool
	siteCmd = &cobra.Command{
		Use:   "site",
		Short: "Abre os horrorosos sites da UFABC",
		Run: func(cmd *cobra.Command, args []string) {
			// refact, do we have PM? Switch/case?
			if tidia {
				openBrowser("https://tidia4.ufabc.edu.br/portal/relogin")
				os.Exit(0)
			} else if prograd {
				openBrowser("https://prograd.ufabc.edu.br/")
				os.Exit(0)
			} else if gradmat {
				openBrowser("https://gradmat.ufabc.edu.br/")
				os.Exit(0)
			} else if bcc {
				openBrowser("https://bcc.ufabc.edu.br")
				os.Exit(0)
			} else if sigaa {
				openBrowser("https://sig.ufabc.edu.br/sigaa/verTelaLogin.do")
				os.Exit(0)
			} else if moodle {
				openBrowser("https://moodle.ufabc.edu.br/")
				os.Exit(0)
			} else if neuro {
				openBrowser("https://neuro.ufabc.edu.br/")
				os.Exit(0)
			} else if ufabc {
				openBrowser("https://www.ufabc.edu.br/")
				os.Exit(0)
			}

			if len(args) == 0 {
				cmd.Help()
			}
		},
	}
)

func init() {

	siteCmd.Flags().BoolVarP(
		&tidia, "tidia",
		"t", false, "abre o site do tidia",
	)

	siteCmd.Flags().BoolVarP(
		&prograd, "prograd",
		"p", false, "abre o site da prograd",
	)

	siteCmd.Flags().BoolVarP(
		&gradmat, "gradmat",
		"g", false, "abre o site do gradmat",
	)

	siteCmd.Flags().BoolVarP(
		&sigaa, "sigaa",
		"s", false, "abre o site do sigaa",
	)

	siteCmd.Flags().BoolVarP(
		&moodle, "moodle",
		"m", false, "abre o site do moodle",
	)

	siteCmd.Flags().BoolVarP(
		&ufabc, "ufabc",
		"u", false, "abre o site da ufabc",
	)

	siteCmd.Flags().BoolVarP(
		&bcc, "bcc",
		"b", false, "abre o site do bcc",
	)

	siteCmd.Flags().BoolVarP(
		&neuro, "neuro",
		"n", false, "abre o site da neuro",
	)

	rootCmd.AddCommand(siteCmd)
}
