package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "nyx",
	Short: "Fear the Nyx.",
	Long:  `A [N]asty, [Y]outhful and [X]enogeneic CLI made for UFABC community.`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Hello CLI")
	},
}

func Execute() {
	cobra.CheckErr(rootCmd.Execute())
}
